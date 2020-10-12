# DEMO Phases

## Phase 1

### With Error

1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name phase-1-sns-with-error --template-body file://sns-cfn.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
2. Run the command:
     ``` shell
     sls deploy
     ```
3. To test it all use the commands:
    ``` shell
    bash sendMessagesNew.sh
    bash sendMessagesOld.sh
    ```

### Error Handling

1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name phase-1-sns-error-handling --template-body file://sns-cfn.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
2. Run the command:
     ``` shell
     sls deploy
     ```
3. To test it all use the commands:
    ``` shell
    bash sendMessagesNew.sh
    bash sendMessagesOld.sh
    ```


## Phase 2


### Deploy Database
1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name demo-database-dynamo --template-body file://dynamo.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
### With Error

1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name phase-2-with-error --template-body file://sqs-cfn.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
2. Run the command:
     ``` shell
     sls deploy
     ```

### Error Handling

1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name phase-2-error-handling --template-body file://sqs-cfn.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
2. Run the command:
     ``` shell
     sls deploy
     ```

## Phase 3


### Deploy Kinesis
1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name demo-kinesis-stream --template-body file://kinesis.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
### With Error
1. Run the command:
     ``` shell
     sls deploy
     ```

### Error Handling
1. Run the command:
   ``` shell
   aws cloudformation create-stack --stack-name phase-3-error-handling --template-body file://dynamo-error-handling-cfn.yml --capabilities CAPABILITY_NAMED_IAM --region=us-east-1
   ```
2. Run the command:
     ``` shell
     sls deploy
     ```