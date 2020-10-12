import boto3
import json
import uuid
import os
from kinesis import KinesisHandler

kinesis = KinesisHandler(os.environ["kinesisName"])
snsArn = os.environ["snsArn"]
retryAttempts = os.environ["retryAttempts"]
sns = boto3.client('sns')

try: 
    eventCounts
except Exception as e:
    eventCounts = dict()


def handler(event, context):
    print(f"event: %s" % json.dumps(event))

    for record in event["Records"]:
        try:
            raise Exception("On purpose error")

            item = dict()
            if("NewImage" in record["dynamodb"].keys()):
                rec = record["dynamodb"]["NewImage"]
                print("New Image")
            elif("OldImage" in record["dynamodb"].keys()):
                rec = record["dynamodb"]["OldImage"]
                print("Old Image")
            else:
                pass     

            item["PurchaseID"] = rec["PurchaseID"]["S"]
            item["PriceID"] = rec["PriceID"]["S"]
            item["UserID"] = rec["UserID"]["S"]
            item["SKU"] = rec["SKU"]["S"]
                        
            kinesis.put_record(item,str(uuid.uuid4()))
        except Exception as e:
            if(record["eventID"] in eventCounts.keys()):
                eventCounts[record["eventID"]] +=1
            else:
                eventCounts[record["eventID"]] = 1

            print("eventCounts[record[\"eventID\"]]: %s" % eventCounts[record["eventID"]])
            print("Max Attempts: %s" % str(int(retryAttempts)+1))

            if(eventCounts[record["eventID"]] == (int(retryAttempts)+1)):
                print("Entrou Envio SNS")
                res = sns.publish(
                    TopicArn=snsArn,
                    Subject=str(e),
                    MessageStructure="json",
                    Message=json.dumps({'default': json.dumps(record)}),
                    )
                print("Response send to sns: %s" % res )
            raise e
    
    