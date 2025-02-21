import boto3
import random
import time

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Example EC2 instance ID (replace with your actual instance ID)
instance_id = 'i-0d0ef5507e74ba9a0'

# Function to send custom metrics tied to EC2 instance
def send_ec2_metric():
    response = cloudwatch.put_metric_data(
        Namespace='EC2CustomMetrics',
        MetricData=[
            {
                'MetricName': 'CustomCPUUsage',
                'Dimensions': [
                    {'Name': 'InstanceId', 'Value': instance_id}
                ],
                'Value': random.uniform(0, 100),  # Simulated CPU usage percentage
                'Unit': 'Percent'
            }
        ]
    )
    print("Custom EC2 metric sent:", response)

# Send the metric every 5 seconds
for _ in range(5):
    send_ec2_metric()
    time.sleep(5)
