import csv
import argparse
import sys

def clean_csv(input_file, output_file):
    """
    Reads a CSV file, removes rows with any empty fields and writes the cleaned data to a new CSV file
    
    Parameters:
    input_file (str): The path to the source CSV file
    output_file (str): The path to the output CSV file
    """
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if all(field.strip() for field in row):
                writer.writerow(row)
                #Checking each row and writes only those rows where all fields have content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Clean CSV by removing rows with empty fields.")
    parser.add_argument('input_file', type=str, help='Path to input CSV file', nargs='?')
    parser.add_argument('output_file', type=str, help='Path to output CSV file', nargs='?')
    args = parser.parse_args()

    if args.input_file is None or args.output_file is None:
        sys.exit() 
        #Exits the script without doing anything if the required arguments are not provided

    clean_csv(args.input_file, args.output_file)
    #Calls the clean_csv function with user provided file paths