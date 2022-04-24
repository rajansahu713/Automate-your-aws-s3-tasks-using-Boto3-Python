import boto3
from os import getenv
from dotenv import load_dotenv
load_dotenv()
s3_resource = boto3.resource('s3', aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))

# Get a list of all buckets names
for bucket in s3_resource.buckets.all():
    print(bucket)


