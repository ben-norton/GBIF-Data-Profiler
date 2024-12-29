import csvkit
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

sourcePath = str(sourcePath) + '/data/' + archiveCode + '/'
# Timestamped output path
targetPath = str(currentPath) + '/csvstats/' + str(ts)

# Create timestamped folder if it doesn't exist
if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

# iterating over all files and generate stats
sourceFiles = str(sourcePath) + "*.csv"
for f in glob.glob(sourceFiles):
    stemName = Path(f).stem
    destFile = archiveCode + '-' + stemName + '-unique-csvstats.csv'
    dest = str(targetPath) + '/' + destFile
    os.system("csvstat -z 10000000 --unique " + f + " > " + dest)
