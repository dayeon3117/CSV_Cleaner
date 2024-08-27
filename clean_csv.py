import csv
import argparse
import sys

def clean_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if all(field.strip() for field in row):
                writer.writerow(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Clean CSV by removing rows with empty fields.")
    parser.add_argument('input_file', type=str, help='Path to input CSV file', nargs='?')
    parser.add_argument('output_file', type=str, help='Path to output CSV file', nargs='?')
    args = parser.parse_args()

    if args.input_file is None or args.output_file is None:
        # Instead of printing a message or exiting, just silently do nothing
        sys.exit()  # Exit quietly

    clean_csv(args.input_file, args.output_file)