# Clean CSV Script Documentation

## Description
This script, `clean_csv.py`, cleans CSV files by removing rows that contain any empty fields.

## Installation
No additional libraries are required, as the script uses only Python’s standard libraries.

## How to Use
To use this script, you need to provide two arguments:
1. `input_file`: The path to the CSV file you want to clean.
2. `output_file`: The path where you want the cleaned CSV file to be saved.

## Troubleshooting
**Error: "the following arguments are required: input_file, output_file"**
- This error occurs if the input and output file paths are not provided when running the script. Make sure to include both paths as shown in the example command:

```bash
python3 clean_csv.py input.csv output.csv