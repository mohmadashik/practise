def sqs_lambda(event,context):
    try:
        print('entry into sqs_lambda ',event)
        message= event['Records'][0]['body']
        small_message = validate_message(message)
        if small_message:
            response = process_message(message)
            print('received proper message')
            return {'status':200,
                    'body':{
                        'message':'success',
                        'response':response
                    }}
        else:
            print('validation error')
            return {'status':403,
                    'body':{
                        'message':'validation error',
                        'response':'length of message is morethan 1000 chars'
                    }}
    except Exception as err:
        print(f'error during sqs_lambda : {err}')

        return {'status':500,
                'body':{
                    'error': str(err)
                }}
def validate_message(message):
    return len(message) < 1000

def process_message(message):
    pass
        