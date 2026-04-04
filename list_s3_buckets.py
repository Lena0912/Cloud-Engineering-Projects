import boto3

def list_my_buckets():
    # Ініціалізація клієнта S3
    s3 = boto3.client('s3')
    
    try:
        response = s3.list_buckets()
        print("--- My AWS S3 Buckets ---")
        for bucket in response['Buckets']:
            print(f"Bucket Name: {bucket['Name']}")
    except Exception as e:
        print(f"Error accessing AWS: {e}")

if __name__ == "__main__":
    list_my_buckets()
