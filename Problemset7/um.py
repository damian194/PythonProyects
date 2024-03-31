import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regular expression to find occurrences of "um" as a whole word (case-insensitive)
    um_pattern = r'\bum\b'
    um_count = len(re.findall(um_pattern, s, re.IGNORECASE))
    return um_count

if __name__ == "__main__":
    main()
