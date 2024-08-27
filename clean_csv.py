import csv

def clean_csv(input_file, output_file):
    """This function reads a CSV file and removes empty rows"""
    with open(input_file, 'r') as file:
        lines = csv.reader(file)
        clean_lines = [line for line in lines if all(field.strip() for field in line)]
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(clean_lines)

#Example usage
clean_csv('example.csv', 'cleaned_example.csv')