import json
import requests
import boto3

webhook = 'https://hooks.slack.com/services/YOUR/KEY/HERE'


def send_to_slack(message):
    """
       Using POST from request library messgae using Webhook from
       Slack API which dumps event from JSON to Python String
       This line allows us to post new messages to your slack channel 
       everytime logs are collected. It prepares and indents the messages
       as a string 
    """
    try:
        r = requests.post(webhook, json.dumps(message, default = 'str', indent=4), headers={'Content-type': 'application/json'})
        r.raise_for_status()
    except requests.exception.ConnectionError as errc:
        raise Exception(errc)
    except requests.exceptions.HTTPError as errh:
        raise Exception(errh)
    except requests.exception.Timeout as errt:
        raise Exception(errt)
    except requests.exception.RequestException as err:
        raise Exception(err)


def format_message(event):
    data = {   
         'attachments': [
            {
                'fields': [
                    {
                        'title': 'Account ID',
                        'value': event['detail']['accountId'],
                        'short': True
                    },
                    {
                        'title' : 'Region',
                        'value' : event['detail']['region'],
                        'short' : True
                     },
                     {
                        'title' : 'Alert Type',
                        'value' : event['detail']['type'],
                        'short' : False
                    },
                    {
                        'title' : 'Instance ID',
                        'value' : event['detail']['resource']['instanceDetails']['instanceId'],
                        'short' : True
                    },
                    {
                        'title' : 'Resource Type',
                        'value' : event['detail']['resource']['resourceType'],
                        'short' : True
                    },
                    {
                        'title' : 'Resource Role',
                        'value' : event['detail']['service']['resourceRole'],
                        'short' : True
                    },
                    {
                        'title' : 'Action type',
                        'value' : event['detail']['service']['action']['actionType'],
                        'short' : True
                    },
                    {
                        'title' : 'Date Alert Created',
                        'value' : event['detail']['createdAt'],
                        'short' : False
                    },
                    {
                        'title' : 'Date Alert Updated',
                        'value' : event['detail']['updatedAt'],
                        'short' : False
                    },
                    {
                        'title' : 'Count',
                        'value' : event['detail']['service']['count'],
                        'short' : True
                    },
                    {
                        'title' : 'Severity Level',
                        'value' : event['detail']['severity'],
                        'short' : True
                    },
                    {
                        'title' : 'Description',
                        'value' : event['detail']['description'],
                        'short' : False
                    }
                ]
            }
        ]
    } 
    send_to_slack(data)
    
def revoke_permissions(event):
    if 'userType' in event['detail']['resource']['accessKeyDetails']:
        # Create IAM client
        iam = boto3.client('iam')
        # Detach a role policy
        iam.detach_role_policy(RoleName= event['detail']['resource']['accessKeyDetails']['userName'],
            PolicyArn= event['detail']['arn']
        )
    

def lambda_handler(event, context):
    # Print logs from CloudWatch
    print(json.dumps(event))
    #currEvent = json.loads(json.dumps(event))
    # for i in event:
    #     data = i
    #     send_to_slack(data)


    format_message(event)


    return {
        'statusCode': 200,
        'body':json.dumps(event),
        'type':str(type(event))

    }
