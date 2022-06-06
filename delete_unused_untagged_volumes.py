import boto3

aws_mag_con = boto3.session.Session(profile_name="WSL_boto3_user")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
unused_ebs_filter = {"Name": "status", "Values": ["available"]}
for each_vol in ec2_con_re.volumes.filter(Filters=[unused_ebs_filter]):
    if not each_volume.tags:
        print(each_vol.id, each_vol.state, each_vol.tags)
        print("Deleting unused and untagged volumes...")
        each_volume.delete()

print("Deleted all unused and untagged volumes")