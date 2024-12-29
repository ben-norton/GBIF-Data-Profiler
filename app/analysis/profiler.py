import json
from dataprofiler import Data, Profiler
from datetime import date
from pathlib import Path
import os
import glob
import csv
import sys

archiveCode = '0049391-241126133413365'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
currentPath = Path().absolute()
sourcePath = currentPath.parent.parent

# Load file (CSV should be automatically identified)
sourceFile = str(sourcePath) + '/data/' + archiveCode + '/occurrence.csv'
targetPath = str(currentPath) + '/output/profiler/' + str(ts)

if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

targetFile = str(targetPath) + '/' + archiveCode + '-profile.json'

# Timestamped output path
data = Data(sourceFile)

# Profile the dataset
profile = Profiler(data)

# Generate a report and use json to prettify.
report  = profile.report(report_options={"output_format": "pretty"})

with open(targetFile, 'w', encoding='utf-8') as f:
    json.dumps(report, f, ensure_ascii=False, indent=4)

# Print the report
#print(json.dumps(report, indent=4))