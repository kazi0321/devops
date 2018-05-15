import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId = "ami-6871a115",
    InstanceType = "t2.micro",
    MinCount = 1,
    MaxCount = 2,
)
