import pandas as pd
import csv
import csv
from datetime import date
from pathlib import Path

# Archive Identifier
archiveCode = '0049395-241126133413365'

today = date.today()
ts = today.strftime("%Y%m%d")

currentPath = Path().absolute()
sourcePath = currentPath.parent.parent

# Source Tab-delimited File
sourceFile = str(sourcePath) + '/data/' + archiveCode + '/occurrence.txt'
# Target CSV File
targetFile = str(sourcePath) + '/data/' + archiveCode + '/occurrence.csv'

def tsv_to_csv(tsv_file, csv_file):
    csv.field_size_limit(100000000)
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter='\t')

        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(tsvreader)

tsv_to_csv(sourceFile, targetFile)
print('successfully converted')