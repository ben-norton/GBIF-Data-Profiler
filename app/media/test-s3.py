import globals as cfg
import yaml
import boto3
from botocore.retries import bucket

root_dir = cfg.get_project_root()

config_yaml = str(root_dir) + '/.aws/config.yml'
with open(config_yaml, 'r') as f:
	config = yaml.safe_load(f)

s3 = boto3.client(
    's3',
	region_name=config['region'],
    aws_access_key_id=config['aws_access_key_id'],
    aws_secret_access_key=config['aws_secret_access_key']
)

response = s3.list_buckets()
for b in response.get("Buckets",None):
    print(b.get("Name",None))
