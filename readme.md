# Wordly v0.1

 Wordly is a Python script designed to generate custom wordlists for cybersecurity and penetration testing purposes. Whether you're doing password audits, brute-force attacks or need home-made wordlists for security assessments, Wordly can create wordlists based on your specific requirements.

---

## Features

- **Customizable Word Lengths:** Specify the minimum and maximum number of letters for each word in your list.
- **Letter Selection:** Choose the exact set of letters to be used for generating words.
- **Output Flexibility:** Save your generated wordlist to a file of your choice for easy access and reuse.
- **Simple Command-Line Interface:** Easily interact with the script using command-line arguments.

## Planned Features

- **Graphical User Interface (GUI):** Launch a user-friendly interface with the `--gui` argument.
- **Wildcard Support:** Use the `-w` argument to include wildcards in your wordlists:
    - `@` or `,` for lowercase and uppercase letters
    - `%` for digits
    - `^` for symbols
- **File size controls:** Limit the maximum size of the generated wordlist using `-M <size>[K|M|G]` (e.g., `-M 10M` for 10 megabytes).
- **Pattern-based Generation:** Allows users to specify patterns (e.g., `a??d` to generate words starting with 'a' and ending with 'd').
- **Compression Support:** Option to save the output as a compressed file (e.g., `.zip` or `.gz`) with `--zip` or `--gz`.
- **Parallel Processing:** Use multiple CPU cores to speed up generation for very large lists.
- **Generation presets:** Use `-p` to create a preset in JSON or `-P` to load a preset file.

---

## How to Use

To get started, run the script with the required arguments.

```bash
python3 wordly.py <min-letters> <max-letters> <letters> <output-file>
```

To display the help menu:

```bash
python3 wordly.py -h
```

To display the version:

```bash
python3 wordly.py -v
```

---

## Example

Suppose you want to generate all possible words between 4 and 6 letters long, using only the letters `a, b, c, d, e`, and save the results to `output.txt`. You would run:

```bash
python3 wordly.py 4 6 abcde output.txt
```

---

> [!NOTE]
> Wordly is in early development and may change significantly in future updates. If you need a stable and feature-rich wordlist generator, consider using [Crunch](https://www.kali.org/tools/crunch/). This project aims to replicate Crunch in Python as a learning exercise.

> [!WARNING] 
> Generating large wordlists (with many letters and long word lengths) can create very large files and may use a lot of system resources.