import json
def topic_subscriber(event,context):
    print(f'entry into topic_subscriber, event : {json.dumps(event,indent=2)}')
    message = event.get('message')
    topic = event.get('topic')
    print(f'topic : {topic}')
    print(f'message : {message}')
    return {'message':message, 'topic':topic,'status_code':200}