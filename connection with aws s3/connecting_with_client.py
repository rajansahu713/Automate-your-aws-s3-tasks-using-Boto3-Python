import boto3
from os import getenv

s3 = boto3.client('s3', aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))


response = s3.list_buckets()
for Bucket in response['Buckets']:
    print(f"Bucket name: {Bucket['Name']}")