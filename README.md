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

| Criterion                                          | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict    |
| -------------------------------------------------- | ------ | ----- | ----- | ----- | ----- | ----- | ---------- |
| 1. matching query completes                        | 4 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)  |
| 2. impossible query stops early                    | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)  |
| 3. session state consistency                       | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)  |
| 4. fit card includes correct price                 | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)  |
| 5. maximum price constraint                        | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)  |
| empty wardrobe (diagnostic — not one of your five) | N/A    | PASS  | PASS  | PASS  | PASS  | PASS  | PASS (5/5) |

**Real output from one try, including the source file and function:**

### Criterion 1 — Matching Query Completes

Source: `agent.py::run_agent`

Query: `vintage graphic tee under $30`

Selected item: Y2K Baby Tee — Butterfly Print ($18.00, depop)

Trace:

    [1] search_listings
          in: dict with keys: description, size, max_price
          out: 10 items: Y2K Baby Tee — Butterfly Print,
               Graphic Tee — 2003 Tour Bootleg Style,
               Vintage Band Tee — Faded Grey … +7 more

    [2] suggest_outfit
          in: dict with keys: item, wardrobe
          out: Here are two ways to style your new Y2K butterfly baby tee...

    [3] create_fit_card
          in: dict with keys: outfit_suggestion, item
          out: Channel your inner 2000s pop star...

Fit card:

Channel your inner 2000s pop star with this dreamy Y2K butterfly baby tee, available now on depop for just $18.00! Whether you're pairing it with baggy denim and a cropped zip hoodie for peak streetwear contrast or tucking it into khaki trousers with combat boots for an edgy earth-tone vibe, this top is effortlessly versatile. ✨🦋

### Criterion 2 — Impossible Query Stops Early

Source: `agent.py::run_agent`

Query: `designer ballgown size XXS under $5`

Actual output:

    stopped early: yes
    selected_item: (none)
    search_results: 0

    [1] search_listings
          in: dict with keys: description, size, max_price
          out: [] (empty)

Error message:

I couldn't find any clothing listings matching your search. Try using a broader description, changing your size, or increasing your maximum budget.

### Criterion 3 — Session State Consistency

Source: `verify_criteria.py::verify_state_consistency`

Additional verification output:

    Try 1: PASS | selected ID: lst_002 | received ID: lst_002
    Try 2: PASS | selected ID: lst_002 | received ID: lst_002
    Try 3: PASS | selected ID: lst_002 | received ID: lst_002
    Try 4: PASS | selected ID: lst_002 | received ID: lst_002
    Try 5: PASS | selected ID: lst_002 | received ID: lst_002

All five verification runs confirmed that the selected item's ID matched the ID received by suggest_outfit.

### Criterion 4 — Fit Card Includes Correct Price

Source: `tools.py::create_fit_card`

Selected item: Y2K Baby Tee — Butterfly Print

Selected item price: $18.00

Actual fit card:

Channel your inner 2000s pop star with this dreamy white, pink, and purple butterfly baby tee! Grab it now on depop for just $18.00 to complete your ultimate Y2K streetwear vibe. Style it with baggy jeans and chunky sneakers, or throw on a black cropped zip hoodie for chilly days.

All five evaluation runs included the correct price of $18.00.

### Criterion 5 — Maximum Price Constraint

Source: `verify_criteria.py::verify_maximum_price`

Query: `vintage graphic tee under $20`

Actual output from Try 1:

    Try 1: PASS | Max price: $20.0 | Results: 8
      - Y2K Baby Tee — Butterfly Print: $18.0
      - Vintage Band Tee — Faded Grey: $19.0
      - Mesh Long-Sleeve Top — Black: $15.0
      - Oversized Crewneck Sweatshirt — Vintage Navy: $20.0
      - Leather Belt — Brown, Braided: $12.0
      - Henley Long Sleeve — Washed Burgundy: $16.0
      - Vintage Polo Shirt — Forest Green: $18.0
      - Bucket Hat — Reversible, Brown Plaid: $14.0

All eight returned listings were priced at or below $20.

The additional verification passed 5 out of 5 runs.

### Empty Wardrobe — Diagnostic

Source: `agent.py::run_agent`

Query: `denim jacket under $50`

Wardrobe: empty

Actual output:

Your wardrobe is currently empty, so I can't create a personalized outfit using clothes you already own. You could style this item with neutral trousers, comfortable sneakers, and a simple jacket. Add items to your wardrobe for personalized suggestions.

All five runs returned non-empty styling advice without crashing.

### Evaluation Note

Criteria 3 and 5 were explicitly verified using a separate
`verify_criteria.py` test after the original baseline evaluation.

The original `run_eval.py --label before` execution did not print
the item-ID comparison or every returned listing's price.

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

## Loop Trace

### Happy Path

Command:

```bash
python app.py ask "vintage graphic tee under $30" --trace
```

Actual output:

```text
[1] search_listings
      in: dict with keys: description, size, max_price
      out: 10 items: Y2K Baby Tee — Butterfly Print,
           Graphic Tee — 2003 Tour Bootleg Style,
           Vintage Band Tee — Faded Grey … +7 more

[2] suggest_outfit
      in: dict with keys: item, wardrobe
      out: Here are two ways to style your new Y2K butterfly baby tee...

[3] create_fit_card
      in: dict with keys: outfit_suggestion, item
      out: Channel your inner 2000s pop star...
```

The agent completed all three tools and generated a fit card.

### Empty Search

Command:

```bash
python app.py ask "designer ballgown size XXS under $5" --trace
```

Actual output:

```text
[1] search_listings
      in: dict with keys: description, size, max_price
      out: [] (empty)
```

The planning loop stopped before calling suggest_outfit or create_fit_card.

### MCP Integration

I replaced the direct Python call to search_listings with
mcp_client.call_tool().

Before:

Agent → search_listings()

After:

Agent → MCP Client → MCP Server → search_listings()

The MCP server exposes search_listings using FastMCP.

The MCP client successfully discovered the tool, including its
description and typed parameters.

The agent continued to complete end-to-end queries after the
MCP integration.

The remaining two tools, suggest_outfit and create_fit_card,
are still called directly.


---

## The Improvement

**What I changed:**

I improved the search relevance logic in `tools.py::search_listings`.

Previously, the search algorithm calculated a relevance score based
on the number of overlapping keywords between the user's query
and each listing.

This caused unrelated products to appear in the results.

For example, searching for "vintage graphic tee under $20"
returned eight listings, including a leather belt and a bucket hat.

I added clothing-type matching using a predefined synonym dictionary.
The search now checks whether the requested clothing type matches
the listing title before applying keyword-overlap ranking.

I kept the existing price filter, size filter, and result limit unchanged.

**Which failure it was meant to fix:**

The improvement targeted the search tool's relevance problem.

The original search algorithm treated all matching keywords equally,
without distinguishing clothing categories from descriptive words.

As a result, a product could appear in the results simply because
its description contained a word such as "vintage".

The new clothing-type check reduces unrelated search results.

### Run Log — After

| Criterion                          | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict      |
| ---------------------------------- | ------ | ----- | ----- | ----- | ----- | ----- | ------------ |
| 1. matching query completes        | 4 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| 2. impossible query stops early    | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| 3. session state consistency       | 5 of 5 | TBD   | TBD   | TBD   | TBD   | TBD   | NOT VERIFIED |
| 4. fit card includes correct price | 5 of 5 | PASS  | PASS  | PASS  | PASS  | PASS  | MET (5/5)    |
| 5. maximum price constraint        | 5 of 5 | TBD   | TBD   | TBD   | TBD   | TBD   | NOT VERIFIED |
| empty wardrobe (diagnostic)        | N/A    | PASS  | PASS  | PASS  | PASS  | PASS  | PASS (5/5)   |

**Did it help, and how do I know:**

Yes. The search returned fewer unrelated products after the change.

For the query "vintage graphic tee under $20":

Before:
- 8 listings returned.
- Results included unrelated products such as a leather belt
  and a bucket hat.

After:
- 3 listings returned.
- The leather belt and bucket hat no longer appeared.
- The selected item remained Y2K Baby Tee — Butterfly Print ($18.00).

For the query "vintage graphic tee under $30":

Before:
- 10 listings returned.

After:
- 5 listings returned.

The original matching query still completed all three tools
in five out of five runs.

The empty-search branch continued to stop correctly in five
out of five runs.

All five generated fit cards continued to include the correct
selected-item price of $18.00.

The results indicate improved search relevance without regressions
in the three criteria that were directly verifiable from the run logs.

---

## What's Still Broken

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

The original five acceptance criteria passed during the baseline
evaluation, with Criteria 3 and 5 confirmed through additional
verification.

The After evaluation also showed successful full executions,
correct empty-search branching, and accurate fit-card prices.

However, several limitations remain.

### 1. Search Relevance Is Still Rule-Based

The search system now uses clothing-type matching to reduce
unrelated results.

However, it still relies on predefined synonyms and
keyword-overlap scoring.

For example, a user might search for "pullover" while a listing
uses the word "sweatshirt". If the synonym dictionary does not
recognize that relationship, the search may miss the item.

A future improvement would use semantic search or embeddings
to recognize similar clothing descriptions.

### 2. Some Search Results Are Still Loosely Related

After the improvement, the query "vintage graphic tee under $20"
returned three listings:

- Y2K Baby Tee — Butterfly Print
- Vintage Band Tee — Faded Grey
- Vintage Polo Shirt — Forest Green

Although the first two are relevant, the vintage polo shirt
is not necessarily a graphic tee.

This happens because the synonym-based matching treats
different shirt types as related.

A stricter clothing-category classification system could
improve the precision of the results.

### 3. Empty Wardrobe Recommendations Are Generic

When the user's wardrobe is empty, the agent provides
general styling advice.

For example, when recommending a denim jacket, the fallback
suggested pairing it with another jacket.

This response is not particularly useful because the selected
item is already a jacket.

A future improvement would generate fallback suggestions
based on the selected item's clothing category.

### 4. Evaluation Coverage

The original acceptance criteria measure successful execution,
empty-search behavior, session consistency, correct prices,
and maximum-price filtering.

They do not directly measure search relevance.

I would add a new criterion requiring at least four out of five
returned listings to match the user's requested clothing type
across several different queries.

### Why I Stopped Here

I focused on making one isolated improvement and measuring
its effect using the same evaluation scenarios.

The change reduced unrelated search results while preserving
the existing tool execution flow.

Additional improvements would require expanding the synonym
dictionary, introducing semantic retrieval, and creating new
evaluation scenarios.

I left those changes for future development to keep this
experiment focused and measurable.
---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
