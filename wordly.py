import sys
from itertools import product

###### VERSION ######
app_version = "0.1"
#####################

def main():
    # Check for arguments
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: python3 wordly.py <min-letters> <max-letters> <letters> <output-file>")
        print("Example: python3 wordly.py 2 4 abc output.txt")
        print("Generates all combinations of the specified letters with lengths from min-letters to max-letters.\n\n   -h, --help: Show this help message\n\n   -v, --version: Show version information\n\n   If no arguments are provided, the program will exit.")
        sys.exit(0)
    
    if sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print(f"Wordly version {app_version}")
        sys.exit(0)

    try:
        min_letters = int(sys.argv[1])
        max_letters = int(sys.argv[2])
        letters = sys.argv[3]
        output_file = sys.argv[4]
    except:
        print("Usage: python3 wordly.py <min-letters> <max-letters> <letters> <output-file>")
        sys.exit(1)

    with open(output_file, 'w') as file:
        for length in range(min_letters, max_letters + 1):
            for combo in product(letters, repeat=length):
                word = ''.join(combo)
                file.write(word + '\n')

if __name__ == "__main__":
    main()