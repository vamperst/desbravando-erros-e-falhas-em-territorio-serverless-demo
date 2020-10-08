import json

def handler(event, context):
    print(f"event: %s" % json.dumps(event))
    
    textMessage = json.loads(event["Records"][0]["Sns"]["Message"])["TextMessage"]

    print(f"Text Message to send: %s" % textMessage)
