def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar_str):
        dollars = float(dollar_str.replace("$", ""))
        return dollars


def percent_to_float(percent_str):
        percent = float(percent_str.replace("%", "")) / 100
        return percent

main()