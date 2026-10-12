# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Three or four sentences: what a user asks for, and what they get back. -->



---

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

### `search_listings`

- **What it does: Search the listings data for items matching a description, and optionally a size and a price ceiling.** 
- **Inputs: description: str, size: str, max_price: float** <!-- name and type each: `max_price` (float), not "a price" -->
- **Returns: A list of listing dicts, each with id, title, description, category, style_tags (list), size,        condition, price (float), colors (list), brand (str or None), platform**
- **When it has nothing: If search_listings returns an empty list, put a message in the session and stop. Otherwise, take the first result and go to suggest_outfit.**

### `suggest_outfit`

- **What it does: Given a thrifted item and the user's wardrobe, suggest one or two outfits.**
- **Inputs:new_item: dict, wardrobe: dict**
- **Returns: A non-empty string with outfit suggestion.**
- **When it has nothing: With an empty wardrobe, return general styling advice rather than raising or returning ""**

### `create_fit_card`

- **What it does: Write a short caption someone would actually post about the find.**
- **Inputs:outfit: str, new_item: dict**
- **Returns: A non-empty string with A two-to-four sentence caption.**
- **When it has nothing: If `outfit` is empty or whitespace, return a descriptive message rather than raising**

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:**

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** <!-- regex, string splitting, or asking the model — say which -->

**What moves through the session:** <!-- which fields, in what order -->

---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python app.py ask 'vintage graphic tee under $30'
The planning loop isn't built yet — see the TODO in agent.py.
```

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]
```

```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))""

Here are two versatile outfit ideas using your new vintage Levi's 501s and pieces you already own:

**Outfit 1: Effortless Everyday Streetwear**
*   **Top:** White ribbed tank top (`w_003`) — *Tuck it in to highlight the waist of the 501s.*
*   **Outerwear:** Vintage black denim jacket (`w_006`) — *Creates a classic denim-on-denim look with contrasting washes.*
*   **Shoes:** Chunky white sneakers (`w_007`)
*   **Accessories:** Brown leather belt (`w_009`) + Black crossbody bag (`w_010`)

**Outfit 2: Cozy & Casual**
*   **Top:** Oversized grey crewneck sweatshirt (`w_004`) — *Let it drape loosely over the straight-leg fit of the jeans.*
*   **Shoes:** Black combat boots (`w_008`) — *Cuff the hems of the 501s slightly to let the boots stand out.*
*   **Accessories:** Black crossbody bag (`w_010`)
```

```
python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

You can never go wrong with a classic pair of vintage Levi's 501 jeans in the absolute best medium wash. Throw them on with some fresh white sneakers for that effortlessly cool, laid-back streetwear vibe. Grab this timeless staple right now on depop for just $38.00 before someone else snatches them up!
```

---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for: I asked ChatGPT to help me implement the three tools in tools.py based on the provided specifications: search_listings, suggest_outfit, and create_fit_card.*
- *What came back: ChatGPT suggested an implementation for search_listings that filters listings by size and maximum price, then ranks the remaining listings using keyword overlap. It also helped implement the two model-based tools for generating outfit suggestions and fit cards.*
- *What I changed: I tested each tool separately instead of assuming the generated code worked. During testing, I found that the model-based tools failed because google.genai was not available in my Python environment. I set up the project environment and dependencies before continuing. I also checked the search results manually to understand how keyword matching could return loosely related items.*

**Moment 2**

- *What I asked for: I gave ChatGPT the starter code and instructions for agent.py and asked how to implement Milestone 5’s planning loop and session state.*
- *What came back: ChatGPT suggested storing each tool’s result in the session and reading it back before calling the next tool. It also suggested a branch that stops the agent when search_listings returns an empty list.*
- *What I changed: I tested both paths with python agent.py. The matching query successfully went through search, outfit generation, and fit-card generation. The impossible query stopped after the search and left session["fit_card"] as None. I used these test results to verify that the branch and session-state behavior matched the project requirements.*


## Planning Loop

**Location:** `agent.py::run_agent`

**Branch rule:** After calling `search_listings`, if no matching listings are
returned, the agent stops and tells the user to change the description, size,
or maximum price. Otherwise, it selects the first result, stores it in the
session, generates an outfit suggestion, and then creates a fit card.
<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion                                          | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict      |
| -------------------------------------------------- | ------ | ----- | ----- | ----- | ----- | ----- | ------------ |
| 1. matching query completes                        | 4 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| 2. impossible query stops early                    | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| 3. session state consistency                       | 5 of 5 | TBD   | TBD   | TBD   | TBD   | TBD   | NOT VERIFIED |
| 4. fit card includes correct price                 | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| 5. maximum price constraint                        | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| empty wardrobe (diagnostic — not one of your five) | N/A    | PASS  | PASS  | PASS  | PASS  | PASS  | PASS (5/5)   |

**Real output from one try**, pasted as text, naming the file and function
that produced it:

```

```

---

## Verdicts and Diagnoses

| #   | Criterion                                     | Target | Verdict   | How I decided                                                                                                                   |
| --- | --------------------------------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Matching query completes all three tools      | 4 of 5 | MET (5/5) | All five runs completed search_listings, suggest_outfit, and create_fit_card successfully.                                      |
| 2   | Impossible query stops before the second tool | 5 of 5 | MET (5/5) | All five runs returned empty search results and stopped before suggest_outfit.                                                  |
| 3   | Session state consistency                     | 5 of 5 | MET (5/5) | An additional verification test confirmed that the selected item ID matched the ID received by suggest_outfit in all five runs. |
| 4   | Fit card includes correct product price       | 5 of 5 | MET (5/5) | All five fit cards included the selected item's correct price of $18.00.                                                        |
| 5   | Maximum price constraint                      | 5 of 5 | MET (5/5) | An additional verification test confirmed that all eight returned listings were priced at or below $20 in all five runs.        |

### Diagnoses

All five acceptance criteria met their targets.

The planning loop correctly handled matching and empty searches,
maintained consistent session state, and generated fit cards
containing accurate product prices.

The maximum-price filter also behaved consistently across
the five verification runs.

However, the evaluation revealed a limitation in search relevance.
For the query "vintage graphic tee under $20", the search returned
items such as a leather belt and a bucket hat.

Although these items satisfied the price constraint, they did not
closely match the requested clothing category.

This suggests that keyword-overlap ranking does not adequately
enforce product-category relevance.

For a future evaluation, I would add a stricter criterion requiring
the returned items to match the requested clothing category.
---

---

## Loop Trace

**Happy path**

Command:

```bash
python app.py ask "vintage graphic tee under $30" --trace
```

Actual output:

```text
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 5 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Vintage Band Tee — Faded Grey … +2 more

[2] suggest_outfit
      in:  dict with keys: item, wardrobe
      out: Here are two ways to style your new Y2K butterfly baby tee using pieces already in your wardrobe:  **Outfit 1:…

[3] create_fit_card
      in:  dict with keys: outfit_suggestion, item
      out: Channel your inner early-2000s pop star with this dreamy pink and purple butterfly baby tee, up now on depop f…
```

Selected item: Y2K Baby Tee — Butterfly Print ($18.00, depop)

Fit card:

```text
Channel your inner early-2000s pop star with this dreamy pink and purple butterfly baby tee, up now on depop for just $18.00! Nail the ultimate Y2K streetwear vibe by pairing it with baggy jeans and a cropped zip hoodie, or mix in some edge by tucking it into khaki trousers with combat boots.
```

The agent completed all three steps successfully. The search tool returned five matching listings, the agent selected the first item, and the remaining two tools generated an outfit suggestion and fit card.

**Empty search**

Command:

```bash
python app.py ask "designer ballgown size XXS under $5" --trace
```

Actual output:

```text
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: [] (empty)
```

Error message:

```text
I couldn't find any clothing listings matching your search.
Try using a broader description, changing your size,
or increasing your maximum budget.
```

The agent stopped immediately after `search_listings` returned an empty list. Neither `suggest_outfit` nor `create_fit_card` was executed.

**On the MCP move:**

Before the MCP integration, `agent.py::run_agent` called `search_listings` directly from `tools.py`.

After the integration, the agent uses `mcp_client.call_tool()` to communicate with the MCP server.

The execution flow changed from:

```text
Agent
  |
  v
tools.py::search_listings()
```

To:

```text
Agent (agent.py::run_agent)
  |
  v
MCP Client (mcp_client.py)
  |
  v
MCP Server (mcp_server.py)
  |
  v
search_listings (tools.py)
  |
  v
Search Results
  |
  v
Agent
  |
  +--> suggest_outfit()
  |
  +--> create_fit_card()
```

The MCP server exposes `search_listings` using FastMCP. The agent sends the parsed description, size, and maximum price through the MCP client and receives a list of matching clothing listings.

The MCP integration was successful. The client discovered the registered tool, and the agent completed the full three-step workflow without requiring changes to the outfit-generation or fit-card-generation tools.

The empty-search branch also continued to work correctly after the MCP integration.

The main architectural difference is that the search tool is now accessed through the MCP protocol instead of a direct Python function call.

---

## The Improvement

**What I changed:**

I improved the search relevance logic in `tools.py::search_listings`.

Previously, the search algorithm ranked listings using simple keyword overlap. Any item sharing at least one keyword with the user's query could appear in the results, even if it belonged to an unrelated clothing category.

For example, searching for "vintage graphic tee under $20" returned eight listings, including a leather belt and a bucket hat.

I added a clothing-type matching rule using a dictionary of related clothing terms. The search now checks whether the requested clothing type matches a recognized term in the listing's title before ranking the results.

I kept the existing price filter, size filter, and result limit unchanged.

**Which failure it was meant to fix:**

The improvement targeted a relevance problem in `tools.py::search_listings`.

All five original acceptance criteria met their targets during the baseline evaluation, but the search results revealed a weakness that those criteria did not directly measure.

The original algorithm treated descriptive words such as "vintage" as equally important as clothing-type words such as "tee".

Consequently, unrelated products could appear in the results simply because they shared a descriptive keyword.

The new clothing-type matching rule aims to reduce these irrelevant results without breaking the existing agent workflow.

### Run Log — After

- Produced by: `run_eval.py::main`

- Loop: `agent.py::run_agent`

- Tools: `tools.py`

- Tries per scenario: 5

- Caching: Off

- Temperature: 0.9

- Date: October 11, 2026, 21:04

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |

|---|---|---|---|---|---|---|---|

| 1. matching query completes | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

| 2. impossible query stops early | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

| 3. session state consistency | 5 of 5 | TBD | TBD | TBD | TBD | TBD | NOT VERIFIED |

| 4. fit card includes correct price | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

| 5. maximum price constraint | 5 of 5 | TBD | TBD | TBD | TBD | TBD | NOT VERIFIED |

| empty wardrobe (diagnostic) | N/A | PASS | PASS | PASS | PASS | PASS | PASS (5/5) |

Criteria 3 and 5 require additional verification after the code change. The evaluation trace confirms the selected item and tool execution, but it does not print the actual item IDs passed between tools or the prices of every returned listing.

### Before vs. After Comparison

| Measurement | Before | After | Result |

|---|---|---|---|

| Graphic tee search under $30 | 10 listings | 5 listings | Fewer loosely related results |

| Graphic tee search under $20 | 8 listings | 3 listings | Fewer loosely related results |

| Leather belt returned | Yes | No | Improved |

| Bucket hat returned | Yes | No | Improved |

| Full three-tool execution | 5/5 | 5/5 | Maintained |

| Empty-search handling | 5/5 | 5/5 | Maintained |

| Correct fit-card price | 5/5 | 5/5 | Maintained |

| Empty-wardrobe handling | 5/5 | 5/5 | Maintained |

### Real Output — Before

Source: `run_eval.py::main` and `agent.py::run_agent`

Query: `vintage graphic tee under $20`

```text

[1] search_listings

      in: dict with keys: description, size, max_price

      out: 8 items: Y2K Baby Tee — Butterfly Print,

           Vintage Band Tee — Faded Grey,

           Mesh Long-Sleeve Top — Black … +5 more

```

The additional baseline verification displayed these eight listings:

```text

Y2K Baby Tee — Butterfly Print: $18.0

Vintage Band Tee — Faded Grey: $19.0

Mesh Long-Sleeve Top — Black: $15.0

Oversized Crewneck Sweatshirt — Vintage Navy: $20.0

Leather Belt — Brown, Braided: $12.0

Henley Long Sleeve — Washed Burgundy: $16.0

Vintage Polo Shirt — Forest Green: $18.0

Bucket Hat — Reversible, Brown Plaid: $14.0

```

### Real Output — After

Source: `run_eval.py::main` and `agent.py::run_agent`

Query: `vintage graphic tee under $20`

```text

[1] search_listings

      in:  dict with keys: description, size, max_price

      out: 3 items: Y2K Baby Tee — Butterfly Print,

           Vintage Band Tee — Faded Grey,

           Vintage Polo Shirt — Forest Green

[2] suggest_outfit

      in:  dict with keys: item, wardrobe

      out: Here are two ways to style your new Y2K butterfly baby tee using pieces already in your wardrobe: ...

[3] create_fit_card

      in:  dict with keys: outfit_suggestion, item

      out: Channel your inner 2000s pop star with this dreamy white, pink, and purple butterfly baby tee...

```

Selected item:

```text

Y2K Baby Tee — Butterfly Print ($18.00, depop)

```

Fit card:

```text

Channel your inner 2000s pop star with this dreamy white, pink, and purple butterfly baby tee, yours for just $18.00 on depop! Serve ultimate off-duty streetwear vibes by pairing it with baggy jeans and a black denim jacket, or lean into edgy casual by styling it with wide-leg trousers and combat boots. Grab this quintessential Y2K staple before it's gone! 🦋✨

```

**Did it help, and how do I know:**

Yes. The improvement reduced unrelated search results while preserving the observed behavior of the main agent workflow.

For the query "vintage graphic tee under $20", the number of returned listings decreased from eight to three. Unrelated accessories, including the leather belt and bucket hat, were removed.

For the query "vintage graphic tee under $30", the number of results decreased from ten to five.

The selected item remained the Y2K Baby Tee — Butterfly Print, priced at $18.00.

The agent also continued to complete all three tools successfully in five out of five runs. The impossible-query branch continued to stop correctly in five out of five runs, and all five fit cards included the correct selected-item price.

These results demonstrate improved search precision for the tested queries.

However, reducing the number of results does not necessarily improve recall. Additional evaluation with more queries would be needed to determine whether the stricter matching rule excludes relevant products.

---


<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->
## What's Still Broken

The baseline evaluation met all five original acceptance criteria, including additional verification of session consistency and maximum-price filtering.

The After evaluation confirmed that the agent still completed full queries, handled empty searches, and generated fit cards with accurate prices. Session consistency and complete price filtering still require explicit post-change verification.

Although the search improvement reduced irrelevant results, several limitations remain.

### 1. Search Relevance

The search system still relies on predefined clothing-type synonyms and keyword-overlap scoring.

For example, the query "vintage graphic tee under $20" still returned "Vintage Polo Shirt — Forest Green".

Although a polo shirt is related to a tee, it is not necessarily a graphic T-shirt.

The current synonym mapping is therefore too broad for some clothing categories.

I would improve this by distinguishing exact clothing types from related alternatives or introducing semantic search with embeddings.

### 2. Search Recall

The new clothing-type rule checks product titles for recognized keywords.

This can exclude relevant products whose titles use different terminology.

For example, a relevant pullover might not appear in a hoodie search if its title does not contain one of the recognized synonyms.

I would evaluate recall using a larger set of queries before making the matching rules stricter.

### 3. Empty Wardrobe Recommendations

When the user's wardrobe is empty, the agent provides general styling advice instead of failing.

However, the recommendations are not always appropriate for the selected item.

For example, the query "denim jacket under $50" produced this suggestion:

```text

Your wardrobe is currently empty, so I can't create a personalized outfit using clothes you already own. You could style this item with neutral trousers, comfortable sneakers, and a simple jacket. Add items to your wardrobe for personalized suggestions.

```

The recommendation suggests another jacket even though the selected item is already a denim jacket.

I would improve the empty-wardrobe prompt to avoid recommending another item of the same clothing type unnecessarily.

### 4. Evaluation Coverage

The original five criteria measure successful tool execution, empty-search handling, session consistency, price accuracy, and maximum-price filtering.

They do not directly measure search relevance or recommendation quality.

In a future evaluation, I would add criteria measuring:

- Clothing-type relevance across different search queries.

- Search recall for synonyms and alternative descriptions.

- Whether outfit recommendations contain appropriate clothing combinations.

- Whether generated suggestions reference only items available in the user's wardrobe.

### Why I Stopped Here

I focused on implementing and evaluating one isolated improvement, as required by Milestone 5.

The change reduced unrelated search results without causing failures in the three acceptance criteria directly verifiable from the After logs.

I did not modify the outfit-generation prompts or add another search algorithm because multiple simultaneous changes would make it difficult to determine which modification caused an improvement or regression.

Further improvements would require additional evaluation scenarios and a more comprehensive relevance-testing framework.
---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
