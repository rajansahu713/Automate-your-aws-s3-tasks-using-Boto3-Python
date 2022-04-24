import boto3
import boto3
from os import getenv
from dotenv import load_dotenv
load_dotenv()

s3 = boto3.resource('s3', aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))
s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')