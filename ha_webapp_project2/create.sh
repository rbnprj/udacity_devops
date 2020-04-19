#Script to create stack in AWS

aws cloudformation create-stack \
--stack-name $1 \
--template-body file://$2 \
--parameters file://$3 \
--capabilities CAPABILITY_IAM \
--region=us-east-1