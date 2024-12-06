import unittest
import pandas as pd
from io import StringIO
from solution import create_contact_index, find_duplicates 

class TestContactFunctions(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        self.valid_data = pd.DataFrame([
            {"contactID": 1, "name": "Alice", "name1": "Smith", "email": "alice@example.com", "postalZip": "12345", "address": "123 Main St"},
            {"contactID": 2, "name": "Bob", "name1": "Jones", "email": "bob@example.com", "postalZip": "67890", "address": "456 Elm St"},
            {"contactID": 3, "name": "Alice", "name1": "Smith", "email": "alice@example.com", "postalZip": "12345", "address": "123 Main St"}
        ])
        self.empty_data = pd.DataFrame(columns=["contactID", "name", "name1", "email", "postalZip", "address"])
        self.malformed_data = """contactID,name,email,postalZip
            1,John Doe,john@example.com,12345
            2,"Unclosed quote,incomplete,row
            """


    def test_create_contact_index_happy_path(self):
        """Test index creation with valid data."""
        contact = {"name": "Alice", "name1": "Smith", "email": "alice@example.com", "postalZip": "12345", "address": "123 Main St"}
        index = create_contact_index(contact)
        self.assertIsInstance(index, str)
        self.assertEqual(len(index), 32)  # MD5 hash length

    def test_create_contact_index_missing_fields(self):
        """Test index creation with missing fields."""
        contact = {"name": None, "name1": "", "email": None, "postalZip": None, "address": ""}
        index = create_contact_index(contact)
        self.assertIsInstance(index, str)
        self.assertEqual(len(index), 32)

    def test_find_duplicates_happy_path(self):
        """Test finding duplicates with valid data."""
        duplicates = find_duplicates(self.valid_data)
        self.assertFalse(duplicates.empty)
        self.assertEqual(len(duplicates), 2)  # Two rows for the duplicate entries

    def test_find_duplicates_no_duplicates(self):
        """Test finding duplicates when there are none."""
        unique_data = self.valid_data.drop(index=2)  # Remove the duplicate
        duplicates = find_duplicates(unique_data)
        self.assertTrue(duplicates.empty)

    def test_find_duplicates_empty_data(self):
        """Test finding duplicates with an empty DataFrame."""
        duplicates = find_duplicates(self.empty_data)
        self.assertTrue(duplicates.empty)

    def test_file_read_errors(self):
        """Test file handling errors."""
        with self.assertRaises(pd.errors.EmptyDataError):
            pd.read_csv(StringIO(""))  # Simulate reading an empty file

        with self.assertRaises(pd.errors.ParserError):
            pd.read_csv(StringIO(self.malformed_data))  # Simulate malformed data


if __name__ == '__main__':
    unittest.main()
