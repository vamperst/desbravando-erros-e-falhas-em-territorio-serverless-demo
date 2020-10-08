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
    ``