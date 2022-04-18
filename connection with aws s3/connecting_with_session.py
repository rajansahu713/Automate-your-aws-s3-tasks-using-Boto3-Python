import boto3
from os import getenv

session = boto3.Session(aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket)

s_2 = session.client('s3')
response = s_2.list_buckets()
for Bucket in response['Buckets']:
    print(f"Bucket name: {Bucket['Name']}")

