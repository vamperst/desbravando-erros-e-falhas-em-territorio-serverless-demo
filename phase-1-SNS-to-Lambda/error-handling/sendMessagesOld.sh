#!/bin/bash

snsTopic=$(aws ssm get-parameter --name "/demo/sns/arn/error/handling" --output text --query Parameter.Value)

for i in 1 2 3 4 5; do
    snsPublished=$(aws sns publish --topic-arn  $snsTopic --message "{\"TextMessage\": \"Troféu ouro conquistado $i\"}")
    echo $snsPublished
done
