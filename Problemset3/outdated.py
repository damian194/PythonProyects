# List of month names
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

# Function to convert a date to YYYY-MM-DD format
def convert_date(input_date):
    try:
        parts = input_date.split('/')
        if len(parts) == 3:
            month, day, year = map(int, parts)
        else:
            # Try to parse the date with month names and a comma
            parts = input_date.split(', ')
            if len(parts) == 2:
                month_day, year = parts
                month, day = month_day.split(' ')
                month = months.index(month) + 1
                day = int(day)
                year = int(year)
            else:
                # Try to parse the date with month names 
                parts = input_date.split(' ')
                if len(parts) == 3:
                    month, day, year = parts
                    month = months.index(month) + 1
                    day = int(day)
                    year = int(year)
                else:
                    raise ValueError("Invalid date format")

        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError("Invalid date")

        return f"{year:04d}-{month:02d}-{day:02d}"

    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

# Prompt the user for a date until a valid one is provided
while True:
    user_input = input("Date: ")
    formatted_date = convert_date(user_input)
    if formatted_date:
        print(formatted_date)
        break



