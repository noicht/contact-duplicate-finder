# Contact Duplicate Finder

This project provides a solution for identifying potential duplicate contacts in a dataset. The main functionalities include creating a unique index for each contact based on relevant fields and finding duplicates based on this index.

## Code Overview

The code consists of two main functions:

1. **create_contact_index(contact)**: 
   - This function generates a unique index for a contact by normalizing relevant fields (name, name1, email, postalZip, and address) and combining them into a single string. 
   - It handles empty fields by replacing them with "n/a" to ensure consistency.
   - The combined string is then hashed using the MD5 algorithm to create a unique identifier.

2. **find_duplicates(contacts)**:
   - This function takes a DataFrame of contacts and applies the `create_contact_index` function to generate a contact index for each entry.
   - It groups the contacts by their index and filters out groups with more than one contact, indicating potential duplicates.
   - The function returns a DataFrame containing the details of the duplicate contacts.

## Optimization

The code is optimized for performance by:
- Using vectorized operations provided by the Pandas library, which are generally faster than iterating through rows manually.
- Grouping contacts by their unique index, which allows for efficient filtering of duplicates.

## Time Complexity

- The time complexity of `create_contact_index` is O(n), where n is the number of contacts, as it processes each contact once.
- The `find_duplicates` function also has a time complexity of O(n) for generating the contact index and O(n) for grouping and filtering, resulting in an overall complexity of O(n).

## How to Run

1. **Prerequisites**:
   - Ensure you have Python installed on your machine.
   - Install the required libraries by running:
     ```bash
     pip install pandas
     ```

2. **Prepare the Data**:
   - Create a CSV file named `contacts.csv` in the same directory as the script. The CSV should contain the following columns: `contactID`, `name`, `name1`, `email`, `postalZip`, and `address`.

3. **Run the Script**:
   - Execute the script using the command:
     ```bash
     python3 solution.py
     ```

4. **Output**:
   - The script will print the contents of the DataFrame and indicate whether any duplicate contacts were found.

## Testing

The project includes a set of unit tests to verify the functionality of the contact index creation and duplicate finding. To run the tests, execute:
```bash
python3 -m unittest -v solution_test.py