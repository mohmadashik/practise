import boto3
import json
def file_upload_handler(event,context):
    try:
        print(f'entry into file_upload_handler, event: {json.dumps(event,indent=2)}')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['objects']['key']
        s3_client = boto3.client('s3')

        response = s3_client.get_object(bucket=bucket,key=key)
        file = response['Body'].read().decode('utf-8')
        print(f'uploaded file is : {file}')
        return 
    except Exception as err:
        message = f'Error in file_upload_handler : {err} '
        print(message)
        return json.dumps( { 'status_code':500, 'msg' : message })
    
