import json 
import base64
import ast
from datetime import datetime 
import boto3

def lambda_handler(event, context): for record in event['Records']:
#Kinesis data is base64 encoded so decode here payload=str(base64.b64decode(record["kinesis"]["data"]),'utf-8') print(payload)
yu={} yu=ast.literal_eval(payload)
#for converting string decoded data to dict. print(type(yu))
for p in yu: 
print(yu[p]) 
yut=list(yu.values()) 
eg=json.dumps(yut)
print(yut)
 length=len(yut) 
 length12=length-2 
 h=0
while h < length12:

string1=json.dumps(yut[h]) 
print(string1) 
print(type(string1))
 string2=string1.split(',') 
 print(string2) 
 data1=string2[1]
 print(data1)
 print(type(data1))
 happys='{'+data1 print(happys)
 #data2=print('{'+sadd)
 #print(data2)
#data1 is the main data to be saved in s3 storage in partition. string3=string2[0].split(':')
print(string3[1])
 string4=string3[1].split(' ') p
 rint(string4)
 hour=string4[2]
 print(hour)
 
date1 = string4[1].replace('"', '')
print(date1)
date2 = datetime.strptime(date1, '%Y-%m-%d') 
q3=(date2.month)
q2=date2.year 
q4=date2.day
client = boto3.client('s3')
client.put_object(Body=happys, Bucket='sar11',Key='year={}/month={}/day={}/{}.json'.format(q2,q3,q4,hour)) h += 1
