import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Instance details
instance_id = "i-03ed67f8318a56fe6"  # Updated instance ID
instance_profile_name = "EC2_Automation_Role"  # Use the correct existing profile

# Attach the instance profile to the EC2 instance
response = ec2_client.associate_iam_instance_profile(
    IamInstanceProfile={"Name": instance_profile_name},
    InstanceId=instance_id
)

print(f"✅ Successfully attached {instance_profile_name} to EC2 instance {instance_id}")
