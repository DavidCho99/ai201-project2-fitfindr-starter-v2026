"""
The FitFindr planning loop.

Unit 4, Milestone 2:
- MCP integration
- Failure handling
- Execution tracing
- Session state management

The agent decides which tool to execute next based on
the results of the previous step.
"""

import re

import config
import trace

from tools import suggest_outfit, create_fit_card
from generate import ModelUnavailable
from mcp_client import call_tool


# ─────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────

def new_session(query: str, wardrobe: dict) -> dict:
    """
    Create a fresh session for one user interaction.

    Every tool result is stored in the session so that
    subsequent steps can access the previous results.
    """

    return {
        "query": query,
        "parsed": {},
        "search_results": [],
        "selected_item": None,
        "wardrobe": wardrobe,
        "outfit_suggestion": None,
        "fit_card": None,
        "error": None,
    }


# ─────────────────────────────────────────────────────────────
# PLANNING LOOP
# ─────────────────────────────────────────────────────────────

def run_agent(query: str, wardrobe: dict) -> dict:
    """
    Execute the FitFindr planning loop.

    Steps:
    1. Parse user query
    2. Search clothing listings through MCP
    3. Branch if no results
    4. Select an item
    5. Generate outfit suggestion
    6. Generate fit card
    """

    session = new_session(query, wardrobe)

    # ─────────────────────────────────────────────────────────
    # STEP 1: PARSE USER QUERY
    # ─────────────────────────────────────────────────────────

    size = None
    max_price = None
    description = query

    price_match = re.search(
        r"\b(?:under|below|max(?:imum)?(?:\s+price)?(?:\s+of)?)\s*\$?(\d+(?:\.\d{1,2})?)",
        query,
        re.IGNORECASE,
    )

    if price_match:
        max_price = float(price_match.group(1))

        description = (
            description[:price_match.start()]
            + " "
            + description[price_match.end():]
        )

    size_match = re.search(
        r"\bsize\s+([A-Za-z0-9/]+)",
        description,
        re.IGNORECASE,
    )

    if size_match:
        size = size_match.group(1)

        description = (
            description[:size_match.start()]
            + " "
            + description[size_match.end():]
        )

    description = re.sub(
        r"\b(?:looking\s+for|find\s+me|i\s+want|i'm\s+looking\s+for)\b",
        " ",
        description,
        flags=re.IGNORECASE,
    )

    description = description.replace(",", " ")
    description = " ".join(description.split())

    session["parsed"] = {
        "description": description,
        "size": size,
        "max_price": max_price,
    }

    # ─────────────────────────────────────────────────────────
    # STEP 2: SEARCH LISTINGS USING MCP
    # ─────────────────────────────────────────────────────────

    search_inputs = {
        "description": session["parsed"]["description"],
        "size": session["parsed"]["size"],
        "max_price": session["parsed"]["max_price"],
    }

    try:
        session["search_results"] = call_tool(
            "search_listings",
            search_inputs,
        )

        trace.step(
            "search_listings",
            search_inputs,
            session["search_results"],
        )

    except Exception as exc:
        session["error"] = (
            "The clothing search service is currently unavailable. "
            "Please try again later."
        )

        trace.step(
            "search_listings",
            search_inputs,
            {"error": str(exc)},
        )

        return session

    # ─────────────────────────────────────────────────────────
    # STEP 3: BRANCH — EMPTY SEARCH RESULTS
    # ─────────────────────────────────────────────────────────

    if not session["search_results"]:

        session["error"] = (
            "I couldn't find any clothing listings matching your search. "
            "Try using a broader description, changing your size, "
            "or increasing your maximum budget."
        )

        return session

    # ─────────────────────────────────────────────────────────
    # STEP 4: SELECT ITEM
    # ─────────────────────────────────────────────────────────

    session["selected_item"] = session["search_results"][0]

    # ─────────────────────────────────────────────────────────
    # STEP 5: SUGGEST OUTFIT
    # ─────────────────────────────────────────────────────────

    outfit_inputs = {
        "item": session["selected_item"],
        "wardrobe": session["wardrobe"],
    }

    # Graceful fallback for an empty wardrobe.
    # Supports both {"items": []} and an empty dictionary.
    wardrobe_items = session["wardrobe"].get("items", [])

    if not wardrobe_items:
        session["outfit_suggestion"] = (
            "Your wardrobe is currently empty, so I can't create "
            "a personalized outfit using clothes you already own. "
            "You could style this item with neutral trousers, "
            "comfortable sneakers, and a simple jacket. "
            "Add items to your wardrobe for personalized suggestions."
        )

        trace.step(
            "suggest_outfit",
            outfit_inputs,
            session["outfit_suggestion"],
        )

    else:

        try:
            session["outfit_suggestion"] = suggest_outfit(
                session["selected_item"],
                session["wardrobe"],
            )

            trace.step(
                "suggest_outfit",
                outfit_inputs,
                session["outfit_suggestion"],
            )

        except ModelUnavailable as exc:

            session["error"] = (
                "The AI styling service is currently unavailable. "
                "Please try again later. If the problem continues, "
                "check your API configuration."
            )

            trace.step(
                "suggest_outfit",
                outfit_inputs,
                {"error": str(exc)},
            )

            return session

    # ─────────────────────────────────────────────────────────
    # STEP 6: CREATE FIT CARD
    # ─────────────────────────────────────────────────────────

    card_inputs = {
        "outfit_suggestion": session["outfit_suggestion"],
        "item": session["selected_item"],
    }

    try:
        session["fit_card"] = create_fit_card(
            session["outfit_suggestion"],
            session["selected_item"],
        )

        trace.step(
            "create_fit_card",
            card_inputs,
            session["fit_card"],
        )

    except ModelUnavailable as exc:

        session["error"] = (
            "The AI service couldn't generate your fit card. "
            "Please try again later. If the issue continues, "
            "check your API configuration."
        )

        trace.step(
            "create_fit_card",
            card_inputs,
            {"error": str(exc)},
        )

        return session

    return session


# ─────────────────────────────────────────────────────────────
# DISPLAY RESULTS
# ─────────────────────────────────────────────────────────────

def _show(session: dict) -> None:
    """
    Display the final session result.
    """

    if session["error"]:
        print(f"  stopped: {session['error']}")
        print(
            f"  fit_card is {session['fit_card']!r} "
            "— it should still be None here if the run stopped early"
        )
        return

    item = session["selected_item"] or {}

    print(
        f"  found:    {item.get('title')} "
        f"— ${item.get('price')} "
        f"on {item.get('platform')}"
    )

    print(
        f"  outfit:   {session['outfit_suggestion']}"
    )

    print(
        f"  fit card: {session['fit_card']}"
    )


# ─────────────────────────────────────────────────────────────
# RUN EXAMPLES
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":

    from utils.data_loader import get_example_wardrobe

    print("=== A query the data can match ===")

    _show(
        run_agent(
            query="looking for a vintage graphic tee under $30",
            wardrobe=get_example_wardrobe(),
        )
    )

    print("\n=== A query it can't match ===")

    _show(
        run_agent(
            query="designer ballgown size XXS under $5",
            wardrobe=get_example_wardrobe(),
        )
    )

    print(
        "\nThe second query should stop before generating "
        "an outfit or fit card."
    )
