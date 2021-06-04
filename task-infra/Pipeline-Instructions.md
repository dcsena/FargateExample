Run the following AWS CLI command to create your first pipeline:

```bash
aws cloudformation create-stack \
    --stack-name fargateexample-pipeline \
    --template-body file://pipeline.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```

```bash
aws cloudformation update-stack \
    --stack-name fargateexample-pipeline \
    --template-body file://pipeline.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```