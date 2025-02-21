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
            instances.append((instance_id, state))
            print(f"  {idx}. Instance ID: {instance_id}, State: {state}, Type: {instance_type}, Public IP: {public_ip}")

    return instances

# Function to start an EC2 instance
def start_instance(instance_id):
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"\n🚀 Starting instance: {instance_id}")

# Function to stop an EC2 instance
def stop_instance(instance_id):
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f"\n🛑 Stopping instance: {instance_id}")

# List instances and ask user which one to manage
instances = list_instances()

if not instances:
    print("❌ No instances found.")
    exit()

# Ask the user to select an instance by number
while True:
    try:
        selection = int(input("\nEnter the number of the instance you want to manage: ").strip())
        if 1 <= selection <= len(instances):
            instance_id = instances[selection - 1][0]
            break
        else:
            print("❌ Invalid selection. Please enter a valid number from the list.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Ask the user for the action (start or stop)
while True:
    action = input("Enter 'start' to start the instance or 'stop' to stop it: ").strip().lower()
    if action in ["start", "stop"]:
        break
    print("❌ Invalid input. Please enter 'start' or 'stop'.")

# Perform the action
if action == "start":
    start_instance(instance_id)
elif action == "stop":
    stop_instance(instance_id)
