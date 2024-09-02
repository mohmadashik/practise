import boto3

def create_s3_bucket(bucket_name):
	s3 = boto3.client('s3')
	s3.create_bucket(Bucket=bucket_name)

create_s3_bucket('ashik-bucket-123')
	