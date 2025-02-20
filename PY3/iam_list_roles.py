import boto3

# Initialize IAM client
iam_client = boto3.client("iam")

# Function to list IAM roles
def list_iam_roles():
    response = iam_client.list_roles()
    print("\n🔹 Available IAM Roles:")
    for role in response["Roles"]:
        print(f"  - {role['RoleName']} | Created: {role['CreateDate']}")

# Run the function
list_iam_roles()
