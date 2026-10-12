"""
Verify FitFindr acceptance criteria.

Criterion 3:
The selected item's ID must match the item passed
to suggest_outfit in 5 of 5 runs.

Criterion 5:
All returned listings must respect the maximum price
in 5 of 5 runs.
"""

from unittest.mock import patch

import agent
from utils.data_loader import get_example_wardrobe


def verify_state_consistency():
    """Criterion 3: Verify selected-item ID across the tool boundary."""

    print("\n=== Criterion 3: Session State Consistency ===")

    original_suggest_outfit = agent.suggest_outfit

    for attempt in range(1, 6):
        received_items = []

        def spy_suggest_outfit(new_item, wardrobe):
            received_items.append(new_item.copy())
            return original_suggest_outfit(new_item, wardrobe)

        with patch.object(
            agent,
            "suggest_outfit",
            side_effect=spy_suggest_outfit,
        ):
            session = agent.run_agent(
                query="vintage graphic tee under $30",
                wardrobe=get_example_wardrobe(),
            )

        selected_item = session["selected_item"]

        passed = (
            selected_item is not None
            and len(received_items) == 1
            and received_items[0].get("id") == selected_item.get("id")
            and selected_item.get("id") is not None
        )

        status = "PASS" if passed else "FAIL"

        print(
            f"Try {attempt}: {status} "
            f"| selected ID: {selected_item.get('id') if selected_item else None} "
            f"| received ID: {received_items[0].get('id') if received_items else None}"
        )


def verify_maximum_price():
    """Criterion 5: Verify every returned listing's price."""

    print("\n=== Criterion 5: Maximum Price Constraint ===")

    for attempt in range(1, 6):
        session = agent.run_agent(
            query="vintage graphic tee under $20",
            wardrobe=get_example_wardrobe(),
        )

        max_price = session["parsed"]["max_price"]
        results = session["search_results"]

        passed = (
            session["error"] is None
            and len(results) > 0
            and max_price is not None
            and all(
                isinstance(item.get("price"), (int, float))
                and item["price"] <= max_price
                for item in results
            )
        )

        status = "PASS" if passed else "FAIL"

        print(
            f"Try {attempt}: {status} "
            f"| Max price: ${max_price} "
            f"| Results: {len(results)}"
        )

        for item in results:
            print(f"  - {item.get('title')}: ${item.get('price')}")


if __name__ == "__main__":
    verify_state_consistency()
    verify_maximum_price()
