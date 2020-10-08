#!/bin/bash

snsTopic=$(aws ssm get-parameter --name "/demo/sns/arn/with/error" --output text --query Parameter.Value)

for i in 1 2 3 4 5; do
    snsPublished=$(aws sns publish --topic-arn  $snsTopic --message "{\"Message\": \"Troféu ouro conquistado $i\"}")
    echo $snsPublished
done
