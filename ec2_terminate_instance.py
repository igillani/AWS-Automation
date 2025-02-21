import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Function to list all instances and let the user select one for termination
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

# Function to terminate an EC2 instance
def terminate_instance(instance_id):
    ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(f"\n❌ Terminating instance: {instance_id}")

# List instances and ask user which one to terminate
instances = list_instances()

if not instances:
    print("❌ No instances found.")
    exit()

# Ask the user to select an instance by number
while True:
    try:
        selection = int(input("\nEnter the number of the instance you want to terminate: ").strip())
        if 1 <= selection <= len(instances):
            instance_id = instances[selection - 1][0]
            break
        else:
            print("❌ Invalid selection. Please enter a valid number from the list.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Confirm before terminating
confirm = input(f"⚠️ Are you sure you want to terminate instance {instance_id}? (yes/no): ").strip().lower()
if confirm == "yes":
    terminate_instance(instance_id)
else:
    print("❌ Termination cancelled.")
