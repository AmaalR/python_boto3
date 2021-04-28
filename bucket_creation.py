import boto3
import os
import sys
import datetime

#The program to create a bucket using boto3 and to append current date with its name.

#date is stored to current_time
d = datetime.datetime.now()
current_time = "{}{}{}".format(d.month,d.day,d.year)

#creating bucket and appending date
client = boto3.client('s3')
response = client.create_bucket(
    ACL='private',
    #Bucket='amals3',
    Bucket='amals3_{}'.format(current_time),
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-1'
    }
)


