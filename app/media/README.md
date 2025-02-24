# Media Utilities
20250128
A collection of utilities for interacting with media records associated with occurrence records.

```
pip install awscli
aws configure
pip install boto3
```
Set local media directory in the globals.py configuration file

## Scripts
| Script                      | Purpose                                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| get-media.py                | Download all media files listed in a multimedia.txt source datset file to a local directory (specified in globals.py)           |
| get-sample-media.py         | Download up to the first 40 images in a multimedia.txt source file                                                              |
| scans-multimedia-records.py | Scans the multimedia.txt data files in the source-data folder. Results are printed to a markdown table in media_scan_results.md |
| test-s3.csv                 | Test connection to a specific AWS S3 Bucket                                                                                     |
| upload-media.py             | Upload media in specified local media directory to AWS S3 bucket                                                                |