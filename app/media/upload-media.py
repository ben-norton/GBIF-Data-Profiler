import globals as cfg
from pathlib import Path
import boto3
import os

root_dir = cfg.get_project_root()
media_root_dir = cfg.get_media_directory()

dataset_code = 'media'        # Dataset Filter. See globals.py
bucket_name = 'gbif-occurrence-media'
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = str(root_dir) + '/.aws/credentials'
os.environ['AWS_CONFIG_FILE'] = str(root_dir) + '/.aws/config'

datasets = cfg.get_datasets(dataset_code)
session = boto3.Session(profile_name='default')
s3 = session.client('s3',region_name='us-east-1')
s3resource = boto3.resource('s3')

count = 0
for dataset in datasets:
    package_id = dataset
    print(package_id)
    media_dir = str(media_root_dir) + '/' + package_id + '_media'
    images = Path(media_dir).glob('*.jpg')
    for image in images:
        filename = Path(image).name
        s3path = package_id + '/' + filename
        count += 1
        s3resource.Object(bucket_name, s3path).upload_file(image)

print("Number of images uploaded: " + str(count))
