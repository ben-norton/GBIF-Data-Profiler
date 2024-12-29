import csvkit
from datetime import date
from pathlib import Path
import os
import glob
import csv
import sys

archiveCode = '0049395-241126133413365'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
currentPath = Path().absolute()
sourcePath = currentPath.parent.parent

sourcePath = str(sourcePath) + '/data/' + archiveCode + '/'
sourceFile = str(sourcePath) + 'occurrence-b.csv'

# Timestamped output path
targetPath = str(currentPath) + '/csvstats/' + str(ts)

# Create timestamped folder if it doesn't exist
if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

f = sourceFile
stemName = Path(f).stem
destFile = archiveCode + '-' + stemName + '-unique-csvstats.csv'
dest = str(targetPath) + '/' + destFile
os.system("csvstat -z 10000000 --unique " + f + " > " + dest)
