import unittest
import os
import csv
from clean_csv import clean_csv

class TestCleanCSV(unittest.TestCase):
    # test suite for clean_csv.py
    def test_clean_csv_removes_empty_rows(self):
        #Tests whether the clean_csv function correctly removes rows with empty fields
        input_path = 'test_input.csv'
        output_path = 'test_output.csv'
        with open(input_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'city'])
            writer.writerow(['Alice', '30', 'New York'])
            writer.writerow(['', '', '']) #Adding an empty row for the test

        clean_csv(input_path, output_path)

        with open(output_path, 'r') as file:
            reader = list(csv.reader(file))
            self.assertEqual(len(reader), 2) #2 rows: the header and one valid row

        os.remove(input_path)
        os.remove(output_path)
        #Cleans up by removing the test files after the test is complete

if __name__ == '__main__':
    unittest.main()