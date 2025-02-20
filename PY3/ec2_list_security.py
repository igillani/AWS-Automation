import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Function to list security groups
def list_security_groups():
    response = ec2_client.describe_security_groups()
    print("\n🔹 Available Security Groups:")
    for sg in response["SecurityGroups"]:
        print(f"  - {sg['GroupId']} | {sg['GroupName']} | VPC: {sg['VpcId']}")

# Function to list key pairs
def list_key_pairs():
    response = ec2_client.describe_key_pairs()
    print("\n🔹 Available Key Pairs:")
    for key in response["KeyPairs"]:
        print(f"  - {key['KeyName']}")

# List security groups and key pairs
list_security_groups()
list_key_pairs()
