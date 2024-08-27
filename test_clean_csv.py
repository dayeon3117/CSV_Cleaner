import unittest
from clean_csv import clean_csv
import csv

class TestCleanCSV(unittest.TestCase):
    """Test to see if empty rows are removed from the CSV"""
    
    def test_empty_rows_removed(self):
        test_input = 'test_input.csv'
        test_output = 'test_output.csv'
        
        #writing test data
        with open(test_input, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'city'])
            writer.writerow(['Alice', 30, 'New York'])
            writer.writerow(['', '', ''])  # This row is empty and should be removed
        
        #use the function to clean the CSV
        clean_csv(test_input, test_output)
        
        with open(test_output, 'r') as file:
            rows = list(csv.reader(file))
            self.assertEqual(len(rows), 2)  # We expect only two rows (header and Alice's row)

        #clean up files
        import os
        os.remove(test_input)
        os.remove(test_output)

if __name__ == '__main__':
    unittest.main()