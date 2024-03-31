def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0 or x > y:
            raise ValueError

        percentage = (x / y) * 100
        if percentage <= 1:
            return "E"  # empty
        elif percentage >= 99:
            return "F"  # full
        else:
            return round(percentage)
    except ValueError:
        return None

while True:
    input_fraction = input("Fraction: ")

    result = calculate_fuel_percentage(input_fraction)

    if result is None:
        print("Invalid input. Please enter a valid fraction (e.g., 3/4).")
    elif result == "E" or result == "F":
        print(result)
        break
    else:
        print(f"{result}%")




