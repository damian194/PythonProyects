import sys
import os

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            code_lines = 0

            in_multiline_comment = False
            for line in lines:
                line = line.strip()

                if in_multiline_comment:
                    if line.endswith("'''") or line.endswith('"""'):
                        in_multiline_comment = False
                    continue

                if line.startswith("'''") or line.startswith('"""'):
                    in_multiline_comment = True
                    continue

                if line and not line.startswith("#"):
                    code_lines += 1

        return code_lines
    except FileNotFoundError:
        return -1

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Usage: python lines.py <filename.py>")

    filename = sys.argv[1]
    line_count = count_lines(filename)

    if line_count == -1:
        sys.exit(f"File '{filename}' does not exist.")
    else:
        print(f"Number of lines of code in '{filename}': {line_count}")

