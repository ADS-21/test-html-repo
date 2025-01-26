import pandas as pd
import os

# Path to the Excel file
file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'travel_database.xlsx')

try:
    # Load the Excel file
    df = pd.read_excel(file_path)
    print("Excel file loaded successfully.")

    # Check and remove the 'Itinerary' column
    if 'Itinerary' in df.columns:
        df = df.drop(columns=['Itinerary'])
        print("'Itinerary' column removed successfully.")
    else:
        print("'Itinerary' column does not exist in the file.")

    # Save the updated DataFrame back to the same file
    df.to_excel(file_path, index=False)
    print(f"Updated file saved successfully at: {file_path}")

except FileNotFoundError:
    print(f"File not found: {file_path}. Ensure the file exists at this path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


