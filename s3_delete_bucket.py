import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'your-unique-bucket-name-nhdb5'

# Delete an empty bucket
def delete_bucket():
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Deleted bucket '{bucket_name}' successfully.")

# Call the function to delete the bucket
delete_bucket()
