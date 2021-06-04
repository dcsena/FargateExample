```bash
aws cloudformation create-stack \
    --stack-name fargateexampleapi-pipeline \
    --template-body file://pipeline.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```
```bash
aws cloudformation update-stack \
    --stack-name fargateexampleapi-pipeline \
    --template-body file://pipeline.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```
```bash
aws cloudformation describe-stacks \
    --stack-name fargateexampleapi-pipeline \
    --query 'Stacks[].Outputs'
```