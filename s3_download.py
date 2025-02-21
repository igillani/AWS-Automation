import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'your-unique-bucket-name-nhdb5'

# Download a file from S3
def download_file(object_name, download_path):
    s3.download_file(bucket_name, object_name, download_path)
    print(f"Downloaded '{object_name}' to '{download_path}'.")

# Example usage
download_file('uploaded_imran_gillani.pdf', r'C:\Users\imran\Desktop\Downloaded_Imran_Gillani.pdf')
