import boto3
from os import getenv
from dotenv import load_dotenv
load_dotenv()
s3_connector = boto3.client('s3', aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))



def get_file_list(s3_bucket_name="my-new-bucket0987", prefix = ''):
    paginator = s3_connector.get_paginator('list_objects_v2')
    #print(paginator)
    pages = paginator.paginate(Bucket=s3_bucket_name, Prefix=prefix)
    #print(pages)
    res = []
    for page in pages:
        #print(page)
        for obj in page['Contents']:
            res.append((obj['Key'], obj['LastModified']))
    if not res:
        return [], []
    
    res.sort(key=lambda z: z[1])
    # Split into two lists
    keys, last_modified = zip(*res)
    print(keys, last_modified)
    return keys, last_modified

keys, last_modified = get_file_list()