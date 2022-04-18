from boto3.session import Session
from os import getenv
from dotenv import load_dotenv
load_dotenv()


ACCESS_KEY=getenv('AWS_S3_ACCESS_KEY')
SECRET_KEY=getenv('AWS_S3_SECRET_KEY')

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
your_bucket = s3.Bucket(getenv('AWS_S3_BUCKET'))


your_bucket.objects.all().delete()
your_bucket.delete()

