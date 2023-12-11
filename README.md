# CSV Label Processing

Machine learning is fantastic, but dealing with dataset cleaning can be a real challenge. In a recent task involving a dataset, I discovered that the data didn't align with my requirements. Consequently, I found myself spending a considerable amount of time manually cleaning the dataset. The process became particularly daunting when dealing with 40,000 lines of data. That's when I realized the need for a more efficient solution. This code can potentially save you 5 hours of manual work in just 1 minute. This Python script processes a CSV file, renaming labels based on specified conditions. It utilizes the pandas library for data manipulation and analysis.

## What does this code do?

The script reads a CSV file and modifies the labels in the last column based on the following conditions:

- If the label starts with "Android_", it is renamed to "MALWARE."
- If the label is "Benign," it is renamed to "BENIGN."

The changed and unchanged labels are printed to the console.

## Usage

### Prerequisites

- Python 3.x
- [pandas library](https://pandas.pydata.org/)

### Installation

Before running the script, make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

To install the required library, run the following command in your terminal or command prompt:



pip install pandas


## How to Use

1. Clone the repository:
 
   git clone https://github.com/daniyyell-dev/Machine-Learning-Anndroid

   cd Machine-Learning-Anndroid

Note: Make sure the dataset is inside the same folder of this code. 
