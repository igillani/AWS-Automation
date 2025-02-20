import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2")

# Key pair name
key_name = "my-new-keypair"

# Create key pair
response = ec2_client.create_key_pair(KeyName=key_name)

# Save private key to a file
with open(f"{key_name}.pem", "w") as file:
    file.write(response["KeyMaterial"])

print(f"✅ Created Key Pair: {key_name} (Saved as {key_name}.pem)")
