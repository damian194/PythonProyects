import csv
import sys

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input_file.csv output_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Read the input CSV file and write to the output CSV file
        with open(input_file, 'r', newline='') as csvfile_in, open(output_file, 'w', newline='') as csvfile_out:
            reader = csv.DictReader(csvfile_in)
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                # Split the 'name' column into first and last names
                full_name = row['name']
                first_name, last_name = full_name.split(', ')
                # Write the split values to the output CSV
                writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

        print("Conversion completed successfully.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()