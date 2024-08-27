import unittest
import os
import csv
from clean_csv import clean_csv

class TestCleanCSV(unittest.TestCase):
    def test_clean_csv_removes_empty_rows(self):
        input_path = 'test_input.csv'
        output_path = 'test_output.csv'
        with open(input_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'city'])
            writer.writerow(['Alice', '30', 'New York'])
            writer.writerow(['', '', ''])

        clean_csv(input_path, output_path)

        with open(output_path, 'r') as file:
            reader = list(csv.reader(file))
            self.assertEqual(len(reader), 2)

        os.remove(input_path)
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()