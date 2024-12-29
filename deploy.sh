#!/bin/bash

set -e

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null
then
    echo "AWS CLI could not be found. Please install it to proceed."
    exit 1
fi

# Variables
STACK_NAME=${1:-"lfb-s3-stack"}
TEMPLATE_FILE=${2:-"my_bucket.yml"}
REGION=${3:-"eu-west-1"}
BUCKET_NAME=${4:-"lfb-etl-bucket"}

# Deploy the CloudFormation stack
echo "Deploying CloudFormation stack: $STACK_NAME with template: $TEMPLATE_FILE in region: $REGION"
aws cloudformation deploy \
    --template-file $TEMPLATE_FILE \
    --stack-name $STACK_NAME \
    --region $REGION \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides BucketName=$BUCKET_NAME

echo "CloudFormation stack deployed successfully!"
