import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: optimized.py <filepath>")
        return
    filepath = sys.argv[1]

    with open(filepath, "r") as f:
        for line in f:
            print(line.strip())

    print("Fichier traité avec succès.")


if __name__ == "__main__":
    main()
