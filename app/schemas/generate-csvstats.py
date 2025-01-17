import csvkit
from datetime import date
from pathlib import Path
import os
import glob
import csv
import sys
import globals as cfg

dataset_code = 'ypm'
root_dir = cfg.get_project_root()
datasets = cfg.get_datasets(dataset_code)

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = 'verbatim.csv'
    source_type = 'verbatim'

    today = date.today()
    ts = today.strftime("%Y%m%d")

    source_file = str(root_dir) + '/source-data/' + archive_code + '/' + source_filename
    target_path = str(root_dir) + '/app/schemas/csvstats/'
    target_report = str(target_path) + '/' + str(ts) + '-' + archive_code + '-' + source_type + '-' + dataset_code + '-csvstats.txt'


    f = source_file

    # Unique Counts
    #os.system("csvstat -z 10000000 --unique " + f + " > " + dest)

    # Full Stats
    os.system("csvstat -z 10000000 " + f + " > " + target_report)