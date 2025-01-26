import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib

# Path to the dataset
file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'travel_database.xlsx')

# Load the dataset
try:
    df = pd.read_excel(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"File not found: {file_path}. Ensure the file exists at this path.")
    exit()

# Preprocess the data
if 'Itinerary' in df.columns:
    df = df.drop(columns=['Itinerary'])  # Drop the Itinerary column
    print("'Itinerary' column dropped.")

# Encode the categorical column 'Destination Type'
encoder = OneHotEncoder(sparse_output=False)

encoded_types = encoder.fit_transform(df[['Destination Type']])
encoded_columns = encoder.get_feature_names_out(['Destination Type'])
encoded_df = pd.DataFrame(encoded_types, columns=encoded_columns)

# Concatenate the encoded columns with the original DataFrame
df = pd.concat([df.drop(columns=['Destination Type']), encoded_df], axis=1)

# Split features (X) and target (y)
X = df.drop(columns=['Destination'])  # Features
y = df['Destination']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
print("Random Forest Classifier trained successfully.")

# Save the model and encoder
model_path = "model.pkl"
encoder_path = "encoder.pkl"
joblib.dump(clf, model_path)
joblib.dump(encoder, encoder_path)
print(f"Model saved to {model_path}")
print(f"Encoder saved to {encoder_path}")
