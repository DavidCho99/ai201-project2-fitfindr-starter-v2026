import re

import config
from generate import generate
from utils.data_loader import load_listings


# ── Helpers ───────────────────────────────────────────────────────────────────

def _words(text: str) -> set[str]:
    """Convert text into lowercase words for simple keyword matching."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _size_matches(requested_size: str, listing_size: str) -> bool:
    """
    Match clothing sizes without unsafe substring matching.

    Examples:
        M   matches M and S/M
        S   matches S and S/M
        L   does NOT match XL
        S   does NOT match US 9
    """
    requested = requested_size.strip().lower()
    actual = listing_size.strip().lower()

    if requested == actual:
        return True

    # Split combined sizes such as S/M or M/L into separate size tokens.
    parts = [
        part.strip()
        for part in re.split(r"[/,]", actual)
        if part.strip()
    ]

    return requested in parts


# ── Tool 1: search_listings ───────────────────────────────────────────────────

def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search listings using price, size, and keyword overlap.
    Returns the best matches first, or [] when nothing matches.
    """

    listings = load_listings()
    query_words = _words(description)

    scored_results: list[tuple[int, dict]] = []

    for listing in listings:

        # 1. Price filter
        if max_price is not None and listing["price"] > max_price:
            continue

        # 2. Size filter
        if size is not None:
            listing_size = listing.get("size")

            if not listing_size:
                continue

            if not _size_matches(size, listing_size):
                continue

        # 3. Build searchable text from useful listing fields
        searchable_parts = [
            listing.get("title", ""),
            listing.get("description", ""),
            listing.get("category", ""),
            " ".join(listing.get("style_tags", [])),
            " ".join(listing.get("colors", [])),
            listing.get("brand") or "",
        ]

        searchable_words = _words(" ".join(searchable_parts))

        # 4. Keyword-overlap score
        score = len(query_words & searchable_words)

        # Drop zero-score results
        if score == 0:
            continue

        scored_results.append((score, listing))

    # 5. Best keyword matches first
    scored_results.sort(key=lambda result: result[0], reverse=True)

    # 6. Respect configured result limit
    return [
        listing
        for _, listing in scored_results[: config.SEARCH_RESULT_LIMIT]
    ]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """
    Suggest one or two outfits using the new item and the user's wardrobe.
    """

    wardrobe_items = wardrobe.get("items", [])

    item_description = (
        f"Title: {new_item.get('title', 'Unknown item')}\n"
        f"Category: {new_item.get('category', 'Unknown')}\n"
        f"Color: {', '.join(new_item.get('colors', []))}\n"
        f"Style: {', '.join(new_item.get('style_tags', []))}\n"
        f"Size: {new_item.get('size', 'Unknown')}"
    )

    # Empty wardrobe branch
    if not wardrobe_items:
        prompt = f"""
You are a fashion styling assistant.

The user is considering this thrifted item:

{item_description}

The user's wardrobe is empty, so do not pretend they already own any
specific pieces.

Suggest one or two general ways to style this item.
Keep the response concise and practical.
"""

        return generate(prompt).strip()

    # Format existing wardrobe pieces for the model
    formatted_wardrobe = []

    for item in wardrobe_items:
        details = []

        for key, value in item.items():
            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)

            details.append(f"{key}: {value}")

        formatted_wardrobe.append("- " + ", ".join(details))

    wardrobe_text = "\n".join(formatted_wardrobe)

    prompt = f"""
You are a fashion styling assistant.

The user is considering this thrifted item:

{item_description}

The user already owns these wardrobe pieces:

{wardrobe_text}

Suggest one or two outfits using the new thrifted item.

Use specific pieces from the user's wardrobe rather than inventing items
they do not own. Keep the response concise and practical.
"""

    return generate(prompt).strip()


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Create a short social-style caption for the thrift find.
    """

    # Empty outfit guard
    if not outfit or not outfit.strip():
        return (
            "A fit card could not be created because no outfit suggestion "
            "was provided."
        )

    title = new_item.get("title", "thrifted item")
    price = new_item.get("price")
    platform = new_item.get("platform", "the marketplace")

    colors = ", ".join(new_item.get("colors", []))
    style_tags = ", ".join(new_item.get("style_tags", []))

    prompt = f"""
Write a short social-media-style fit card for this thrift find.

Item: {title}
Price: ${price:.2f}
Platform: {platform}
Colors: {colors}
Style: {style_tags}

Outfit suggestion:
{outfit}

Requirements:
- Write 2 to 4 sentences.
- Make it sound like a caption someone would actually post.
- Mention the item.
- Mention the exact price (${price:.2f}) once.
- Mention the platform ({platform}) once.
- Describe a specific vibe.
- Use the provided outfit suggestion.
- Do not invent a different price or platform.
- Do not write a product-description-style list.
"""

    return generate(prompt).strip()
