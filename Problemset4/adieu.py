import inflect

def main():
    p = inflect.engine()
    names = []

    print("Name:")

    # Read names from the user until Ctrl-D (EOF) is encountered
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    num_names = len(names)

    if num_names == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif num_names > 1:
        last_name = names.pop()
        names_str = ", ".join(names)

        if num_names == 2:
            print(f"Adieu, adieu, to {names_str} and {last_name}")
        else:
            print(f"Adieu, adieu, to {names_str}, and {last_name}")

if __name__ == "__main__":
    main()
