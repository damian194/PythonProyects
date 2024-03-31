import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define a regular expression pattern to match the input formats
    pattern = r'^(\d{1,2}:\d{2} (?:AM|PM)) to (\d{1,2}:\d{2} (?:AM|PM))$|^(\d{1,2} (?:AM|PM)) to (\d{1,2} (?:AM|PM))$'

    # Try to match the input string against the pattern
    match = re.match(pattern, s)

    if match:
        # Extract the matched groups
        groups = match.groups()

        if groups[0] is not None:
            start_time = groups[0]
            end_time = groups[1]
        else:
            start_time = groups[2]
            end_time = groups[3]

        # Convert 12-hour format to 24-hour format
        start_time_24 = convert_to_24_hour(start_time)
        end_time_24 = convert_to_24_hour(end_time)

        return f"{start_time_24} to {end_time_24}"
    else:
        raise ValueError("Invalid input format")

def convert_to_24_hour(time_str):
    # Split the time string into hours, minutes, and AM/PM
    time_parts = re.split(r'[: ]', time_str)

    # Extract hours, minutes, and AM/PM
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    am_pm = time_parts[2]

    if am_pm == 'PM' and hours != 12:
        hours += 12
    elif am_pm == 'AM' and hours == 12:
        hours = 0

    # Format the hours and minutes as a 24-hour time string
    return f"{hours:02d}:{minutes:02d}"

if __name__ == "__main__":
    main()
