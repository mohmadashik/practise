import boto3

s3 = boto3.client('s3')

def upload_file(file_path,bucket_name,file_name_in_s3):
    s3.upload_file(file_path,bucket_name,file_name_in_s3)
    print(f'File {file_path} uploaded to {bucket_name} bucket as {file_name_in_s3}')


file_path = 'sample_file.txt'
file_name_in_s3 = 'example_file_sep_2.txt'
bucket_name ='new-bucket-876'

upload_file(file_path,bucket_name,file_name_in_s3)