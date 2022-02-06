import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

response = table.put_item(
    Item={
        'year': 1,
        'title': 'my-document-title',
        'content': 'some-content',
        'director': 'Mike',
        'actor' : 'Joe',
    }
)
