import boto3
import json
import uuid
import os
from kinesis import KinesisHandler

kinesis = KinesisHandler(os.environ["kinesisName"])



def handler(event, context):
    print(f"event: %s" % json.dumps(event))
    
    raise Exception("On purpose error")
    for record in event["Records"]:

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