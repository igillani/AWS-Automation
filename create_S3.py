import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket name must be unique globally
bucket_name = 'your-unique-bucket-name-nhdb5'

# Create a new S3 bucket
def create_bucket():
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-1'  # Replace with your region
        }
    )
    print("Bucket created successfully:", response)

create_bucket()
