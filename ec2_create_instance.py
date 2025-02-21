import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Default values
DEFAULT_AMI = "ami-053a45fff0a704a47"
DEFAULT_INSTANCE_TYPE = "t2.micro"
DEFAULT_KEY_NAME = "new-key-pair"
DEFAULT_SECURITY_GROUP = "default"

# Function to create an EC2 instance
def create_instance(ami_id, instance_type, key_name, security_group):
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group],
        MinCount=1,
        MaxCount=1
    )

    instance_id = response["Instances"][0]["InstanceId"]
    print(f"✅ Launched EC2 Instance: {instance_id}")
    return instance_id

# Ask the user for instance configuration
ami_id = input(f"Enter AMI ID (or press Enter for default {DEFAULT_AMI}): ").strip() or DEFAULT_AMI
instance_type = input(f"Enter instance type (or press Enter for default {DEFAULT_INSTANCE_TYPE}): ").strip() or DEFAULT_INSTANCE_TYPE
key_name = input(f"Enter key pair name (or press Enter for default {DEFAULT_KEY_NAME}): ").strip() or DEFAULT_KEY_NAME
security_group = input(f"Enter security group ID (or press Enter for default {DEFAULT_SECURITY_GROUP}): ").strip() or DEFAULT_SECURITY_GROUP

# Launch the instance
instance_id = create_instance(ami_id, instance_type, key_name, security_group)
