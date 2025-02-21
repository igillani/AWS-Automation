import boto3

# Initialize the CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Function to create an alarm for the custom metric
def create_alarm():
    response = cloudwatch.put_metric_alarm(
        AlarmName='HighActiveDeviceAlarm',
        MetricName='ActiveDevices',
        Namespace='CustomAppMetrics',
        Statistic='Average',
        Period=300,  # Period in seconds (5 minutes)
        EvaluationPeriods=1,  # Number of periods to evaluate
        Threshold=5,  # Trigger alarm if the metric goes above this value
        ComparisonOperator='GreaterThanThreshold',  # Alarm condition
        ActionsEnabled=False  # No automated action for now (e.g., no SNS notifications)
    )
    print("Alarm created successfully.")

# Call the function to create the alarm
create_alarm()
