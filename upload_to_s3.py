import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name (use the one you created earlier)
bucket_name = 'your-unique-bucket-name-nhdb5'

# Upload a file to the S3 bucket
def upload_file(file_path, object_name=None):
    if object_name is None:
        object_name = file_path  # Use the local filename if no custom name is provided
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"File '{file_path}' uploaded as '{object_name}'.")

# Example usage with the updated path and filename
file_path = r'C:\Users\imran\Desktop\New folder\Imran_Gillani (2).pdf'
upload_file(file_path, 'uploaded_imran_gillani.pdf')
