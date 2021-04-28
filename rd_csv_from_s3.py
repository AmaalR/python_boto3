#program to read csv files from s3 using boto3
#'!pip install s3fs' we need to install this module 

import boto3
import pandas as pd


client = boto3.client('s3')


#bucket_name followed by the Key_value
path = 's3://amals34282021/TPGDS.csv'

df = pd.read_csv(path)
df.head()
