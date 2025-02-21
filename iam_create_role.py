import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")
iam_client = boto3.client("iam")

# Instance ID (Replace with actual instance ID)
instance_id = "i-03ed67f8318a56fe6"  # Replace with your running instance ID
iam_role_name = "EC2_Automation_Role"

# Create an instance profile for the IAM role
iam_client.create_instance_profile(InstanceProfileName=iam_role_name)
iam_client.add_role_to_instance_profile(
    InstanceProfileName=iam_role_name,
    RoleName=iam_role_name
)

# Attach the instance profile to the EC2 instance
ec2_client.associate_iam_instance_profile(
    IamInstanceProfile={"Name": iam_role_name},
    InstanceId=instance_id
)

print(f"✅ Attached IAM Role {iam_role_name} to EC2 Instance {instance_id}")
