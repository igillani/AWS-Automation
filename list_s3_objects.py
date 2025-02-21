import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'your-unique-bucket-name-nhdb5'

# List all S3 buckets
def list_buckets():
    response = s3.list_buckets()
    print("Buckets in your AWS account:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

# List all objects in the specific bucket
def list_objects():
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print(f"Objects in bucket '{bucket_name}':")
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print(f"No objects found in bucket '{bucket_name}'.")

# Example usage
list_buckets()
list_objects()
