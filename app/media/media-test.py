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
	return target_dir

for dataset in datasets:
    package_id = dataset
    print(package_id)
    source_file = str(root_dir) + '/source-data/' + package_id + '/multimedia.txt'
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore', dtype=object)
    samples = df.iloc[:40, df.columns.get_loc('identifier')] # Get first 40 records in multimedia file
    samples.to_csv('sample_media.csv', index=False)
    samples_lst = samples.values.tolist()
    target_path = create_dir(package_id)
    shutil.copy(source_file, target_path)
    count = 0
    for img_url in samples_lst:
	    if pd.notna(img_url):
		    a = urlparse(img_url)
		    filename = os.path.basename(a.path)
		    target_file = str(target_path) + '/' + filename
		    response = urllib.request.urlopen(img_url)
		    image = response.read()
		    with open(target_file, 'wb') as f:
			    f.write(image)
		    count += 1

    print("Images Downloaded: " + str(count))



