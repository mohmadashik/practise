import boto3
SNS_TOPIC_ARN = 'aws:accountid:arn link here'

def sns_email_sender(event,context):
    try:
        print('entry into sns_email_sender : ',event)
        sns_client = boto3.client('sns')
        message = event.get('message')
        subject = event.get('subject')
        response = sns_client.publish(
            TopicArn= SNS_TOPIC_ARN,
            Message = message,
            Subject = subject
        )
        return {'status':200,
                'body':{
                    'message':'Email sent successfully',
                    'response':response
                }}
    except Exception as err:
        print(f'error during sqs_lambda : {err}')

        return {'status':500,
                'body':{
                    'error': str(err)
                }}

def ses_email_sender(event,context):
    try:
        print('entry into ses_email_sender : ',event)
        ses_client = boto3.client('ses')
        message = event.get('message')
        subject = event.get('subject')
        recepient = event.get('recepient')
        response = ses_client.send_email(
            Destination = {
                'ToAddresses':[recepient]},

            Message = {
                        'Subject':{'Data':subject},
                        'Body': {
                                'Text':{
                                    'Data':message
                                    }
                                }
                        }
        )

        return {'status':200,
                'body':{
                    'message':'Email sent successfully',
                    'response':response
                }}
    except Exception as err:
        print(f'error during ses_email_sender : {err}')
        return {
                'status':500,
                'body':{
                    'error': str(err)
                }}