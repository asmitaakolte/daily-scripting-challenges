import boto3

def detect_unused_ec2_instances():
    ec2 = boto3.client('ec2')

    # list all EC2 instances
    response = ec2.describe_instances()
    
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            tags = instance.get('Tags', [])
            tag_names = [tag['Key'] for tag in tags]

            # Check if the instance is running or stopped
            if state in ['running', 'stopped']:
                print(f"Instance ID: {instance_id}, State: {state}, Tags: {tag_names}")

if __name__ == "__main__":
    detect_unused_ec2_instances()
    print("Script to detect unused EC2 instances executed successfully.")
    


