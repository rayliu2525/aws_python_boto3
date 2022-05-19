import boto3
aws_man_con = boto3.session.Session(profile_name = "WSL_boto3_user")
ec2_con_client = aws_man_con.client(service_name = "ec2", region_name = "us-east-1")

response = ec2_con_client.describe_instances()
for each_item in response["Reservations"]:
    for each_instance in each_item["Instances"]:
        print(each_instance["InstanceId"])