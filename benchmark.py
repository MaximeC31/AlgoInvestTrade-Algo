import csv
import sys
import time

import matplotlib.pyplot as plt

from bruteforce import bruteforce_algo
from optimized import optimized_algo

BUDGET: float = 500.0
MAX_ACTIONS: int = 21


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


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python benchmark.py <filepath>")
        sys.exit(1)
    filepath: str = sys.argv[1]

    actions = parse_csv(filepath)

    times_bruteForce: list[float] = []
    times_optimized: list[float] = []
    cumul_bruteForce: float = 0.0
    cumul_optimized: float = 0.0
    sizes = list(range(1, min(len(actions), MAX_ACTIONS) + 1))

    for n in sizes:
        subset = actions[:n]

        start = time.time()
        bruteforce_algo(subset, BUDGET)
        cumul_bruteForce += time.time() - start
        times_bruteForce.append(cumul_bruteForce)

        start = time.time()
        optimized_algo(subset, BUDGET)
        cumul_optimized += time.time() - start
        times_optimized.append(cumul_optimized)

        print(
            f"n={n} | BruteForce cumulé: {cumul_bruteForce:.3f}s | Optimized cumulé: {cumul_optimized:.5f}s"
        )

    plt.figure(figsize=(10, 6))  # type: ignore
    plt.plot(sizes, times_bruteForce, "r-o", label="Bruteforce")  # type: ignore
    plt.plot(sizes, times_optimized, "g-o", label="Optimized")  # type: ignore
    plt.xticks(sizes)  # type: ignore
    plt.xlabel("Nombre d'actions (n)")  # type: ignore
    plt.ylabel("Temps d'exécution (secondes)")  # type: ignore
    plt.title("Benchmark : Bruteforce vs Optimized")  # type: ignore
    plt.legend()  # type: ignore
    total_bruteForce = sum(times_bruteForce)
    total_optimized = sum(times_optimized)
    plt.figtext(  # type: ignore
        0.5,
        0.01,
        f"Temps cumulé - Bruteforce : {total_bruteForce:.2f}s | Optimized : {total_optimized:.6f}s",
        ha="center",
        fontsize=9,
    )
    plt.tight_layout(rect=[0, 0.04, 1, 1])  # type: ignore
    plt.savefig("benchmark.png")  # type: ignore
    print("Graphique sauvegardé dans benchmark.png")


if __name__ == "__main__":
    main()
