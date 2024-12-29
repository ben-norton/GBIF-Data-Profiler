import csv
import numpy as np
from datetime import date
from pathlib import Path
import os

archiveCode = '0049391-241126133413365'
analysisType = 'column-lengths'

today = date.today()
ts = today.strftime("%Y%m%d")

currentPath = Path().absolute()
sourcePath = currentPath.parent.parent

# Source Files Path
filename = str(sourcePath) + '/data/' + archiveCode + '/occurrence.csv'

# Timestamped output path
targetPath = str(currentPath) + '/output/' + analysisType + '/' + str(ts)

# Create output path if it doesn't exist
if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

data = []

with open(filename, newline='') as csvfile:
    csv.field_size_limit(100000000)
    reader = csv.reader(csvfile)
    for row in reader:
        data.append([float(value) for value in row])  # Convert to float

# Step 2: Convert to NumPy array
data_array = np.array(data)

# Step 3: Find the maximum of each column
column_max = np.max(data_array, axis=0)

# Step 4: Subtract each value from its corresponding column max
result_array = column_max - data_array

# Print results
print("Column Maxima:", column_max)
print("Resulting Array:\n", result_array)