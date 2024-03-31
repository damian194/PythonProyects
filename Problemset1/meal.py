def main():
    user_input = input("Please enter the time in HH:MM format: ")
    time = convert(user_input)

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print()

def convert(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()

