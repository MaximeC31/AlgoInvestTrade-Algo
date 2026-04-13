import csv
import sys
import itertools

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


def bruteforce_algo(
    actions: list[dict[str, str | float]], budget: float
) -> tuple[tuple[dict[str, str | float]], float, float]:
    initial_budget: float = budget
    combinaisons_total: list[tuple[tuple[dict[str, str | float]], float, float]] = []
    for nb_actions in range(1, len(actions) + 1):
        for combo in itertools.combinations(actions, nb_actions):
            total_cost: float = sum(float(action["price"]) for action in combo)
            if total_cost <= initial_budget:
                total_profit: float = sum(float(a["price"]) * float(a["profit"]) for a in combo)
                remaining_budget: float = initial_budget - total_cost
                combinaisons_total.append((combo, total_profit, remaining_budget))
            print(f"Combinaisons testées : {len(combinaisons_total)}", end="\r")

    combinaisons_total.sort(key=lambda combo: combo[1], reverse=True)
    best_combo, best_profit, best_remaining = combinaisons_total[0]
    return best_combo, best_profit, best_remaining


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python bruteforce.py <filepath>")
        sys.exit(1)
    filepath: str = sys.argv[1]

    actions = parse_csv(filepath)
    best_combo, best_profit, best_remaining = bruteforce_algo(actions, BUDGET)

    print("Actions achetées :")
    for action in sorted(best_combo, key=lambda x: int(str(x["name"]).split("-")[-1])):
        print(f"{action['name']} — {action['price']}€ — {round(float(action['profit']) * 100, 2)}%")
    print(f"Coût total : {BUDGET - best_remaining}€")
    print(f"Bénéfice total : {best_profit}€")


if __name__ == "__main__":
    main()
