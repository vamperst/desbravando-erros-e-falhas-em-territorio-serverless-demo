import boto3
from boto3.dynamodb.conditions import Key
import json


class dynamoDAO:
    def __init__(self, table_name):
        self.__table = boto3.resource('dynamodb').Table(table_name)
        self.__client = boto3.client('dynamodb')
        self.__table_name = table_name


    def put_item(self, item):
        return self.__table.put_item(
            Item=item,
            ReturnConsumedCapacity='TOTAL'
        )

    def get(self, key):
        return self.__table.get_item(
            Key=key
        )