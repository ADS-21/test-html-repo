import pandas as pd
import random
import os

# Define data options
destination_types = ['Continental', 'Domestic', 'Mountain', 'International', 'Beach', 'City', 'Adventure']
destinations = [
    'Paris', 'New York', 'Tokyo', 'Sydney', 'Cape Town', 'Rio de Janeiro', 'Zurich', 
    'Hawaii', 'Maldives', 'Singapore', 'Iceland', 'Alaska', 'Banff', 'Bali', 'Dubai'
]

# Generate synthetic data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        destination_type = random.choice(destination_types)
        destination = random.choice(destinations)
        cost = random.randint(500, 10000)  # Costs in USD
        no_of_days = random.randint(3, 10)
        
        data.append({
            'Destination Type': destination_type,
            'Destination': destination,
            'Cost (USD)': cost,
            'Number of Days': no_of_days
        })
    return data

# Create DataFrame
num_records = 5000
data = generate_data(num_records)
df = pd.DataFrame(data)

# Define output file path
try:
    output_file = os.path.join(os.path.expanduser('~'), 'Documents', 'travel_database.xlsx')
    print(f"Saving file to: {output_file}")
    df.to_excel(output_file, index=False)
    print(f"Data saved successfully to {output_file}")
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied: Unable to write to the specified location.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
