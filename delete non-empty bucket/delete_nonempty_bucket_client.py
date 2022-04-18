import boto3
from os import getenv
from dotenv import load_dotenv
load_dotenv()

s3_client = boto3.client('s3', aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))


contents=s3_client.list_objects(Bucket=getenv("AWS_S3_BUCKET"))['Contents']

contents.delete()

