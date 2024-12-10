import boto3

s3 = boto3.client('s3')

def list_s3_buckets():
    response = s3.list_buckets()
    return response

print('S3 buckets')
all_buckets = list_s3_buckets()
for bucket in all_buckets['Buckets']:
    print(bucket['Name'])

