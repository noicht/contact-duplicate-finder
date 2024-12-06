import pandas as pd
import hashlib

def create_contact_index(contact):
    """Create a unique index for a contact based on relevant fields, handling empty fields."""
    #Normalize empty fields with n/a
    name = contact['name'].lower() if pd.notna(contact['name']) else "n/a"
    name1 = contact['name1'].lower() if pd.notna(contact['name1']) else "n/a"
    email = contact['email'].lower() if pd.notna(contact['email']) else "n/a"
    postal_zip = contact['postalZip'] if pd.notna(contact['postalZip']) else "n/a"
    address = contact['address'].lower() if pd.notna(contact['address']) else "n/a"
    
    combined = f"{name}_{name1}_{email}_{postal_zip}_{address}"
    # Generate a hash of the combined string to create a unique index
    return hashlib.md5(combined.encode()).hexdigest() # I will explain this on the readme file

def find_duplicates(contacts):
    """Find potential duplicates in the contact list based on indexing."""
    if contacts.empty:
        # Return an empty DataFrame with the required structure
        return pd.DataFrame(columns=['contactID', 'name', 'name1', 'email', 'postalZip', 'address'])
    
    contacts['Contact Index'] = contacts.apply(create_contact_index, axis=1)
    
    # Group by the contact index and filter out groups with more than one contact
    duplicates = contacts.groupby('Contact Index').filter(lambda x: len(x) > 1)
    
    duplicates_summary = duplicates[['contactID', 'name', 'name1', 'email', 'postalZip', 'address']]
    
    return duplicates_summary

if __name__ == "__main__":
    file_path = 'contacts.csv'  # Named it contacts.csv for testing purposes, but it can be any file path

    try:
        contacts_df = pd.read_csv(file_path)
        print(contacts_df)
        
        print("Columns in the DataFrame:", contacts_df.columns)
        
        duplicates_df = find_duplicates(contacts_df)
        
        if not duplicates_df.empty:
            print("Duplicate Contacts Found:")
            print(duplicates_df)
        else:
            print("No duplicate contacts found.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")