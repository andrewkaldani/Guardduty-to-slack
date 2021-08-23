# Guardduty-to-slack

# Goal: 
The goal of this project is to send AWS GuardDuty alerts to AWS CloudWatch. Then format the logs using Slack's Block Kits and send them to a Slack Channel. The GuardDuty alerts get passed in through AWS Lambda using python. When certain alerts are detected using the boto3 library it detaches role policies from the user that it detected. 

# Configuration:

# Slack:
1. Create a Slack Channel 
2. After creating a Slack Channel go to the settings page and click incoming webhooks and toggle activate incoming webhooks to on
3. Once a webhook is created pick the channel you want the webhook to be connected to and click authorize to your app. You willl recieve a URL link with some keys at the end of the link make sure you keep that private
4. If you want to test to make sure it posts messages to your slack channel copy the curl requst and run it on your terminal. It should POST "Hello World" to your slack channel.
Resource: https://api.slack.com/messaging/webhooks
# AWS GuardDuty/CloudWatch/Lambda:
You can use this within the free tier of AWS
1. Go to Lambda -> Create Function -> Author from scratch and select Permissions -> Create a new role with basic Lambda permissions. Name the event what you would like
2. When you go to lambda you should see a lambda_handler(event,context) function
3. Go to CloudWatch then to Events, Rules, and create Rule. Select the service name as as GuardDuty and event type as all events
4. Within the same Page click add target and pick your lambda function as the target. 
5. Go to the next page, name it, and create the rule
6. Within the lambda function put print(json.dumps(event))
7. Deploy it, go to test configure the test event, name it test and save.
8. Once tested go to CloudWatch, logs, log groups, click your log
9. Check one log and copy one of the json results from GuardDuty
10. Go back to lambda and put that in the test file
11. Copy the code in lambda
12. Change the slack webhook url to your own url
13. Deploy and test the code
14. Go to GuardDuty, settings, and click generate sample findings. Give it ~5 minutes to send alerts to Slack

