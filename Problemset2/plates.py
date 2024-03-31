def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[:2].isalpha():
        return False

    if not plate[2:].isalnum():
        return False

    if '0' <= plate[-1] <= '9' and plate[2] != '0':
        return True

    return False

main()
