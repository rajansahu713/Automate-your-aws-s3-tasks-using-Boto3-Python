import boto3
from os import getenv

s3 = boto3.resource('s3', aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))


for bucket in s3.buckets.all():
    print(bucket)
