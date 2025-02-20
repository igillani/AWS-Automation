import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Security group details
group_name = "my-secure-group"
group_description = "Security group for SSH and HTTP access"

# Create a new security group
response = ec2_client.create_security_group(
    GroupName=group_name,
    Description=group_description,
    VpcId="vpc-xxxxxxxxxxxxxxxxx"  # Replace with your actual VPC ID
)

security_group_id = response["GroupId"]
print(f"✅ Created Security Group: {security_group_id}")

# Add rules: Allow SSH (22) & HTTP (80) access
ec2_client.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {"IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "IpRanges": [{"CidrIp": "0.0.0.0/0"}]},  # SSH
        {"IpProtocol": "tcp", "FromPort": 80, "ToPort": 80, "IpRanges": [{"CidrIp": "0.0.0.0/0"}]},  # HTTP
    ],
)

print("✅ Added SSH (22) and HTTP (80) rules.")
