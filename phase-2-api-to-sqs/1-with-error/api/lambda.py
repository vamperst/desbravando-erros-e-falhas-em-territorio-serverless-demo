import boto3
import json
from random import randint
from random import randint
import random
import uuid
import os
from dynamo import dynamoDAO




def handler(event, context):
    body = json.loads(event.get('body'))
    print(f"body: %s" % json.dumps(body))
    
    orderNumber = randint(0, 10000000000000)
    hashOrder = uuid.uuid4()
    purchaseID = "{}-{}".format(str(orderNumber),hashOrder)
    body.update({"PurchaseID":purchaseID})
    
    # send to SNS
    sns = boto3.client('sns')
    snsArn=os.environ["snsArn"]

    res = sns.publish(
                    TopicArn=snsArn,
                    Subject="Order Creation",
                    Message=json.dumps(body),
                    )
    
    message={"PurchaseID":purchaseID,"Status":"Created"}
    response = {
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "application/json"
            },
            "statusCode": 201,
            "body": json.dumps(message)
        }

    return response
def storeGameSell(event, context):
    print(f"event: %s" % json.dumps(event))
    try:
        body = json.loads(json.loads(event["Records"][0]["body"])["Message"])
        print(f"body: %s" % json.dumps(body))
        if(bool(random.getrandbits(1))):
            print("Error!!!")
            raise Exception("Random Error generated")
        dao = dynamoDAO(os.environ["dynamoTableName"])

        item = dict()
        item["PurchaseID"]=body["PurchaseID"]
        item["UserID"]=body["UserID"]
        item["SKU"]=body["SKU"]
        item["PriceID"]=body["PriceID"]

        dao.put_item(item)

        print(f"item stored in dynamo: %s" % json.dumps(item))
    except Exception as ex:
        print(ex)
        raise ex
    