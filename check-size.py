import os

file_path = 'DATASET.csv'  # Replace with the actual path to your file
file_size = os.path.getsize(file_path)

# Convert file size to human-readable format
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

print(f"File Size: {convert_bytes(file_size)}")
