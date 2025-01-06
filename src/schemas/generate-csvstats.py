import csvkit
from datetime import date
from pathlib import Path
import os
import glob
import csv
import sys
import config as cfg

root_dir = cfg.get_project_root()
datasets = cfg.get_datasets()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)

    today = date.today()
    ts = today.strftime("%Y%m%d")


    source_file = str(root_dir) + '/source-data/' + archive_code + '/occurrence.csv'
    target_path = str(root_dir) + '/src/schemas/csvstats/' + str(ts)

    # Create timestamped folder if it doesn't exist
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    f = source_file
    destFile = archive_code + '-occurrence-csvstats.csv'
    dest = str(target_path) + '/' + destFile

    # Unique Counts
    #os.system("csvstat -z 10000000 --unique " + f + " > " + dest)

    # Full Stats
    os.system("csvstat -z 10000000 " + f + " > " + dest)