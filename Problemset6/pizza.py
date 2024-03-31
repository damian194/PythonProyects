import sys
import os
import csv
from tabulate import tabulate

def load_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
        return data
    except FileNotFoundError:
        sys.exit(f"Error: File '{file_path}' not found.")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <csv_file_path>")

    # Get the CSV file path from the command line argument
    csv_file_path = sys.argv[1]

    # Check if the file extension is '.csv'
    if not csv_file_path.endswith('.csv'):
        sys.exit("Error: The specified file must have a '.csv' extension.")

    # Check if the specified file exists
    if not os.path.exists(csv_file_path):
        sys.exit(f"Error: File '{csv_file_path}' does not exist.")

    # Load the data from the CSV file
    data = load_csv(csv_file_path)

    # Format and print the table using tabulate
    header = data[0]
    table_data = data[1:]
    table = tabulate(table_data, headers=header, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
