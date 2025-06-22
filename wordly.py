import sys

def main():
    # Check for arguments
    if len(sys.argv) < 4:
        print("Usage: python3 wordly.py <min-letters> <max-letters> <letters> <output-file>")
        sys.exit(1)

    # Parse arguments
    min_letters = int(sys.argv[1])
    max_letters = int(sys.argv[2])
    letters = sys.argv[3]
    output_file = sys.argv[4]

    for i in range(min_letters, max_letters + 1):
        with open(f"{output_file}.txt", "w") as file:
            continue

if __name__ == "__main__":
    main()