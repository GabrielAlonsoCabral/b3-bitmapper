import boto3


def upload_to_s3(local_file_path, bucket_name, s3_key):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the file
    try:
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to {bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")