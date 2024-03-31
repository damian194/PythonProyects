from datetime import date, datetime
import inflect
import sys

# Function to calculate age in minutes
def calculate_age_in_minutes(dob):
    today = date.today()
    age_delta = today - dob
    age_in_minutes = age_delta.days * 24 * 60  # Minutes in a day

    # Consider leap years
    for year in range(dob.year, today.year):
        if is_leap_year(year):
            age_in_minutes += 24 * 60  # Add one day (24 hours * 60 minutes) for each leap year

    return age_in_minutes

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to convert minutes to English words with the first letter capitalized
def minutes_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword='', zero='zero')
    return words.capitalize()

# Function to prompt the user for date of birth and print the age in words
def main():
    try:
        dob_str = input("Date of Birth: ")
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        age_in_minutes = calculate_age_in_minutes(dob)

        # Convert age in minutes to English words with first letter capitalized
        age_words = minutes_to_words(round(age_in_minutes))
        print(f"{age_words} minutes")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

if __name__ == "__main__":
    main()



