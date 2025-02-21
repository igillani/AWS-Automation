import boto3
import time

# Initialize CloudWatch Logs client
logs = boto3.client('logs')

# Define log group and stream names
log_group_name = 'CustomAppLogs'
log_stream_name = 'DeviceActivityLogs'

# Create a log group
def create_log_group():
    try:
        logs.create_log_group(logGroupName=log_group_name)
        print("Log group created successfully.")
    except logs.exceptions.ResourceAlreadyExistsException:
        print("Log group already exists.")

# Create a log stream
def create_log_stream():
    try:
        logs.create_log_stream(
            logGroupName=log_group_name,
            logStreamName=log_stream_name
        )
        print("Log stream created successfully.")
    except logs.exceptions.ResourceAlreadyExistsException:
        print("Log stream already exists.")

# Send a log message
def send_log_message(message):
    timestamp = int(round(time.time() * 1000))  # Current time in milliseconds
    response = logs.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': timestamp,
                'message': message
            }
        ]
    )
    print("Log sent successfully.")

# Execute log creation and sending
create_log_group()
create_log_stream()
send_log_message("Device SM1 connected successfully.")
send_log_message("Device SM2 sent an update.")
