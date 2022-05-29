import boto3

aws_man_con = boto3.session.Session(profile_name = "WSL_boto3_user")
ec2_con_re = aws_man_con.resource(service_name = "ec2", region_name = "us-east-1")
ec2_con_cli = aws_man_con.client(service_name = "ec2", region_name = "us-east-1")

#using resource object
inst_object = ec2_con_re.Instance("i-04abb9c198703096a")
print("Starting instance...")
inst_object.start()
inst_object.wait_until_running()
print("Your instance is now running")

#using client object
ec2_con_cli.start_instances(InstanceIds=["i-04abb9c198703096a"])
waiter = ec2_con_cli.get_waiter("instance_running")
waiter.wait(InstanceIds = ["i-04abb9c198703096a"])
print("Your instance is now running")