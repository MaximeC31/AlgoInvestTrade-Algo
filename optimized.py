import csv
import sys

BUDGET: float = 500.0


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python optimized.py <filepath>")
        sys.exit(1)
    filepath: str = sys.argv[1]

    raw_rows: list[dict[str, str]] = []
    with open(filepath, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            raw_rows.append(row)

    actions: list[dict[str, str | float]] = []
    for row in raw_rows:
        try:
            profit = row["profit"]
            profit = (
                float(profit.strip("%")) / 100
                if profit.strip().endswith("%")
                else float(profit) / 100
            )
            price = float(row["price"])
        except ValueError:
            continue
        if price > 0 and profit > 0:
            actions.append({"name": row["name"], "price": price, "profit": profit})
    actions.sort(key=lambda x: float(x["profit"]), reverse=True)

    remaining_budget: float = BUDGET
    selected_actions: list[dict[str, str | float]] = []
    for action in actions:
        price = float(action["price"])
        if price <= remaining_budget:
            remaining_budget -= price
            selected_actions.append(action)

    print("Actions achetées :")
    for action in sorted(selected_actions, key=lambda x: int(str(x["name"]).split("-")[-1])):
        print(f"{action['name']} — {action['price']}€ — {round(float(action['profit']) * 100, 2)}%")
    total_cost = BUDGET - remaining_budget
    total_profit = sum(float(a["price"]) * float(a["profit"]) for a in selected_actions)
    print(f"Coût total : {round(total_cost, 2)}€")
    print(f"Bénéfice total: {round(total_profit, 2)}€")


if __name__ == "__main__":
    main()
