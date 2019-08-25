import json
import boto3

kinesis = boto3.client('kinesis',aws_access_key_id="******",region_name="ap-south",aws_secret_access_key="******")

def safg():
    data1={
    "t1":{"time":"2019-06-19 1:20","name":"sam"},
    "t2":{"time":"2019-07-19 2:30" ,"partition":"sd2"},
    "t3":{"time":"2019-06-29 3:00","format":"ext4"},
    "t4":{"time":"2019-07-03 4:59","cloud":"aws"},
    "t5":{"time":"2019-05-13 5:20","file":"fstab"},
    "t6":{"time":"2019-01-10 2:09","place":"delhi"},
    "t7":{"time":"2019-02-28 10:09","keyboard":"querty"},
    "t8":{"time":"2019-12-18 12:09","handler":"s@k"},
    "t9":{"time":"2019-11-11 7:02","floor":"2nd"},
    "t10":{"time":"2019-08-20 21:09","containers":"docker"},
    "t11":{"time":"2019-03-07","service":"lambda"}
    }    
    return data1

if __name__ == '__main__':
    i =0
    while (i<10) :
		data=json.dumps(safg())
		print(data)
		kinesis.put_record(
			StreamName="sarthak",
			Data=data,
			PartitionKey="g23dft"
		)
        i = i+1

        