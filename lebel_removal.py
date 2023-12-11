import pandas as pd

def process_csv(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file, header=None)

    # Create an empty list to store changed labels
    changed_labels = []

    # Rename the last column based on your criteria
    df.iloc[:, -1] = df.iloc[:, -1].apply(lambda label: "MALWARE" if label.startswith("Android_") else "BENIGN" if label == "Benign" else (changed_labels.append(label), label))

    # Write the modified DataFrame to a new CSV file
    df.to_csv(output_file, header=None, index=False)

    # Print the labels that were changed
    print("Changed labels:", changed_labels)

    # Print the labels that were not changed
    unchanged_labels = df[df.iloc[:, -1].isin(["MALWARE", "BENIGN"])].iloc[:, -1].tolist()
    print("Unchanged labels:", unchanged_labels)

if __name__ == "__main__":
    # Replace 'Android_Malware.csv' and 'output.csv' with your file names
    input_file = 'Android_Malware.csv'
    output_file = 'Android_Malware_output.csv'

    # Process the CSV file
    process_csv(input_file, output_file)
