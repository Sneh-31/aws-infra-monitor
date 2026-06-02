import boto3
import datetime

ec2 = boto3.client('ec2', region_name='us-east-1')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

def lambda_handler(event, context):
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    stopped = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                Period=1800,
                StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=30),
                EndTime=datetime.datetime.utcnow(),
                Statistics=['Average']
            )
            
            if metrics['Datapoints']:
                avg_cpu = metrics['Datapoints'][0]['Average']
                print(f"Instance {instance_id} avg CPU: {avg_cpu}%")
                
                if avg_cpu < 5.0:
                    ec2.stop_instances(InstanceIds=[instance_id])
                    stopped.append(instance_id)
                    print(f"Stopped idle instance: {instance_id}")
    
    return {
        'statusCode': 200,
        'body': f'Stopped instances: {stopped}'
    }