import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Retrieve instance information
response = ec2_client.describe_instances()

# Process and display instance details
print("🔹 EC2 Instances:")
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"]
        instance_type = instance["InstanceType"]
        public_ip = instance.get("PublicIpAddress", "N/A")
        print(f"  - Instance ID: {instance_id}, State: {state}, Type: {instance_type}, Public IP: {public_ip}")
