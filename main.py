import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()

    print(f"hello hello world {args.name}")
    return 0


if __name__ == "__main__":
    exit(main())
