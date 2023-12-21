import pandas as pd
from scipy.io import arff

# Load the CSV file
csv_file_path = 'word_label_dataset.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to an ARFF format
arff_file_path = 'Dataset-me-WEKA2.arff'  # Replace with the desired output path

with open(arff_file_path, 'w') as arff_file:
    arff_file.write('@RELATION Dataset\n\n')
    for i, column in enumerate(df.columns):
        if column == 'label':
            arff_file.write('@ATTRIBUTE {} {}\n'.format(column.replace(' ', '_'), '{BENIGN,MALWARE}'))
        else:
            arff_file.write('@ATTRIBUTE {} {}\n'.format('_'.join(column.split()), 'REAL' if i != len(df.columns) - 1 else '{BENIGN,MALWARE}'))

    arff_file.write('\n@DATA\n')
    for index, row in df.iterrows():
        arff_file.write(','.join(map(str, row)) + '\n')
