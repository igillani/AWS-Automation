import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Function to list all EC2 instances with numbering
def list_instances():
    response = ec2_client.describe_instances()
    instances = []

    print("\n🔹 Available EC2 Instances:")
    for idx, reservation in enumerate(response["Reservations"], start=1):
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            instance_type = instance["InstanceType"]
            public_ip = instance.get("PublicIpAddress", "N/A")
            instances.append(instance_id)
            print(f"  {idx}. Instance ID: {instance_id}, State: {state}, Type: {instance_type}, Public IP: {public_ip}")

    return instances

# Function to check IAM role attached to an instance
def check_iam_role(instance_id):
    response = ec2_client.describe_iam_instance_profile_associations()

    print("\n🔹 IAM Role Attached to the Selected Instance:")
    for association in response.get("IamInstanceProfileAssociations", []):
        if association["InstanceId"] == instance_id:
            print(f"  ✅ Instance {instance_id} is attached to IAM Role: {association['IamInstanceProfile']['Arn']}")
            return
    print(f"  ❌ No IAM Role found for instance {instance_id}.")

# List instances and ask user which one to check
instances = list_instances()

if not instances:
    print("❌ No instances found.")
    exit()

# Ask the user to select an instance by number
while True:
    try:
        selection = int(input("\nEnter the number of the instance to check IAM role: ").strip())
        if 1 <= selection <= len(instances):
            selected_instance_id = instances[selection - 1]
            break
        else:
            print("❌ Invalid selection. Please enter a valid number from the list.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Check IAM role for the selected instance
check_iam_role(selected_instance_id)
