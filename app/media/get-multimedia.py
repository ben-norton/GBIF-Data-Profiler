import globals as cfg
import pathlib
import pandas as pd
import glob
import os
from urllib.parse import urlparse
import urllib.request
import shutil

root_dir = cfg.get_project_root()
media_dir = cfg.get_media_directory()
dataset_code = 'media'        # Dataset Filter. See globals.py

datasets = cfg.get_datasets(dataset_code)

def create_dir(package_id):
	target_dir = str(media_dir) + '/' + package_id + '_media'
	if not os.path.isdir(target_dir):
		os.mkdir(target_dir)
	return target_path

for dataset in datasets:
    package_id = dataset
    print(package_id)
    source_file = str(root_dir) + '/source-data/' + package_id + '/multimedia.txt'
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore', on_bad_lines='skip', dtype=object)
    length = len(df.index)
    if(length > 0):
	    print('Number of Images: ' + length)
	    media_lst = df['identifier'].tolist()
	    target_path = create_dir(package_id)
	    shutil.copy(source_file, target_path)
	    count = 0
	    for url in media_lst:
		    a = urlparse(url)
		    filename = os.path.basename(a.path)
		    target_file = str(target_path) + '/' + filename
		    urllib.request.urlretrieve(url, target_path)
		    count += 1

print("Number of images downloaded: " + count)



