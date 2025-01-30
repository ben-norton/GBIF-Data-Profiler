import globals as cfg
import yaml
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import S3UploadFailedError
import os
import json

root_dir = cfg.get_project_root()
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = str(root_dir) + '/.aws/credentials'
os.environ['AWS_CONFIG_FILE'] = str(root_dir) + '/.aws/config'

bucket_name = 'gbif-occurrence-media'

session = boto3.Session(profile_name='default')
s3_session = session.client('s3',region_name='us-east-2')

s3 = boto3.client('s3')
response = s3.list_buckets()

def list_contents(bucket):
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(bucket)
    summaries = my_bucket.objects.all()
    print(summaries)
    files = []
    for file in summaries:
        files.append(file.key)
    return json.dumps({"files": files})

#list_contents(bucket_name)
response = s3.list_objects_v2(
    Bucket=bucket_name)


# s3.Object(bucket_name, object_key).upload_file(file_path)