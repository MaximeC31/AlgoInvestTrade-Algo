import csv
import sys

BUDGET: float = 500.0


def parse_csv(filepath: str) -> list[dict[str, str | float]]:
    raw_rows: list[dict[str, str]] = []
    with open(filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            raw_rows.append(row)

    actions: list[dict[str, str | float]] = []
    for row in raw_rows:
        try:
            profit = (
                float(row["profit"].strip("%")) / 100
                if row["profit"].strip().endswith("%")
                else float(row["profit"]) / 100
            )
            price = float(row["price"])
        except ValueError:
            continue
        if price > 0 and profit > 0:
            actions.append({"name": row["name"], "price": price, "profit": profit})
    return actions


def optimized_algo(
    actions: list[dict[str, str | float]], budget: float = 500.0
) -> tuple[list[dict[str, str | float]], float, float]:
    actions = sorted(actions, key=lambda x: float(x["profit"]), reverse=True)

    remaining_budget: float = budget
    selected_actions: list[dict[str, str | float]] = []
    for action in actions:
        price = float(action["price"])
        if price <= remaining_budget:
            remaining_budget -= price
            selected_actions.append(action)

    total_cost: float = budget - remaining_budget
    total_profit: float = sum(float(a["price"]) * float(a["profit"]) for a in selected_actions)
    return selected_actions, total_profit, total_cost


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python optimized.py <filepath>")
        sys.exit(1)
    filepath: str = sys.argv[1]

    actions = parse_csv(filepath)
    selected_actions, total_profit, total_cost = optimized_algo(actions, BUDGET)

    print("Actions achetées :")
    for action in sorted(selected_actions, key=lambda x: int(str(x["name"]).split("-")[-1])):
        print(f"{action['name']} — {action['price']}€ — {round(float(action['profit']) * 100, 2)}%")
    print(f"Coût total : {round(total_cost, 2)}€")
    print(f"Bénéfice total : {round(total_profit, 2)}€")


if __name__ == "__main__":
    main()
