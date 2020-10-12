import boto3
import json

class KinesisHandler:
    def __init__(self,streamName):
        self.__kinesis = boto3.client('kinesis')
        self.__streamName = streamName
    
    def put_record(self, data,partitionKey):
        response = self.__kinesis.put_record(StreamName=self.__streamName, Data=json.dumps(data), PartitionKey=partitionKey)
        print(json.dumps(response))
    
    def __getItarator(self):
        iterator = self.__kinesis.get_shard_iterator(
            ShardId ='shardId-000000000000',
            StreamName=self.__streamName,
            ShardIteratorType='TRIM_HORIZON'
        ) 
        return iterator
    
    def getRecords(self):
        while(True):
            try:
                iterator = self.__getItarator()
                response = self.__kinesis.get_records(
                    ShardIterator=iterator,
                    Limit=1
                )
                print(response)
            except Exception as ex:
                print(ex)