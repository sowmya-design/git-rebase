import boto3
client = boto3.client('s3')
response = client.run_instances(
   ImageId='ami-06b21ccaeff8cd686',
   InstanceType='t2.micro',
   KeyName='devprod',
   MaxCount=1,
   MinCount=2
)
