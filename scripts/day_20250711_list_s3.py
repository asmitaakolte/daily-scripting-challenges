import os 
import boto3


def list_s3_buckets():
    # Create an S3 client
    s3 = boto3.client('s3')

    # List all buckets
    response = s3.list_buckets()

    # Print bucket names
    print("Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

if __name__ == "__main__":
    list_s3_buckets()
    print("Script to list S3 buckets executed successfully.")