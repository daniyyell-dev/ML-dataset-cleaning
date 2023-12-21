import pandas as pd

# Load the CSV file
file_path = 'DATASET.csv'
df = pd.read_csv(file_path)

# Define mapping for labels
label_mapping = {'MALWARE': 1, 'BENIGN': 0}
df['LABEL'] = df['LABEL'].map(label_mapping)

# Extract labels
labels = df['LABEL']

# Convert the entire DataFrame (excluding labels) to binary format
df_binary = df.iloc[:, :-1].applymap(lambda x: 1 if x != 0 else 0)

# Add the original labels back
df_binary['LABEL'] = labels

# Save the updated dataset
output_file_path = 'binary_dataset.csv'
df_binary.to_csv(output_file_path, index=False)
