from datetime import date
import os
import globals as cfg

# This script generates CSV stats for a CSV datasets using the CSVKit Library.
# Files are specified by dataset_code (see globals.py) and package filename (without the extension)

dataset_code = 'ypm'
package_file_stem = 'verbatim'

root_dir = cfg.get_project_root()
datasets = cfg.get_datasets(dataset_code)

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = package_file_stem + '.csv'


    today = date.today()
    ts = today.strftime("%Y%m%d")

    source_file = str(root_dir) + '/source-data/' + archive_code + '/' + source_filename
    target_path = str(root_dir) + '/app/schemas/csvstats/'
    target_report = str(target_path) + '/' + str(ts) + '-' + archive_code + '-' + package_file_stem + '-' + dataset_code + '-csvstats.txt'


    f = source_file

    # Unique Counts
    #os.system("csvstat -z 10000000 --unique " + f + " > " + dest)

    # Full Stats
    os.system("csvstat -z 10000000 " + f + " > " + target_report)