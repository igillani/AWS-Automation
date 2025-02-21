import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'your-unique-bucket-name-nhdb5'

# Delete a file from the bucket
def delete_file(object_name):
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    print(f"Deleted '{object_name}' from bucket '{bucket_name}'.")

# Example usage
delete_file('uploaded_imran_gillani.pdf')
