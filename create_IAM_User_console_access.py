import boto3
from random import choice
import sys

def get_iam_cli_object():
    session = boto3.session.Session(profile_name="WSL_boto3_user")
    iam_cli = session.client(service_name="iam", region_name="us-east-1")
    return iam_cli

def get_password():
    password_len = 10
    password_chars = "abcdefghijkl0123456789!@#$%^&*?"
    return "".join(choice(password_chars) for char in range(password_len))

def main():
    iam_cli = get_iam_cli_object()
    iam_user_name = "practicingboto3@gmail.com"
    password = get_password()
    Policy_ARN = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_cli.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response["Error"]["Code"] == "EntityAlreadyExists":
            print("IAM user with this username already exists")
            sys.exit()
        else:
            print(e)
            sys.exit()
    iam_cli.create_login_profile(UserName=iam_user_name, Password=password, PasswordResetRequired=False)
    iam_cli.attach_user_policy(Username=iam_user_name, PolicyARN=Policy_ARN)
    print(f"IAM Username = {iam_user_name}, Password = {password}")