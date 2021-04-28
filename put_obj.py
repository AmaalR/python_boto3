import boto3
import os
import sys
import datetime


print(os.listdir())


with open("aaa.txt", 'rt') as f:
    data = f.read()    

client = boto3.client('s3')    
response = client.put_object(
    ACL='private',
    Body=data,
    Bucket='amals34282021',
    Key='aaa.txt'
)
