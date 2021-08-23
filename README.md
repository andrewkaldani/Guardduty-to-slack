# Guardduty-to-slack

Goal: The goal of this project is to send AWS GuardDuty alerts to AWS CloudWatch. Then format the logs using Slack's Block Kits and send them to a Slack Channel. The GuardDuty alerts get passed in through AWS Lambda using python. When certain alerts are detected using the boto3 library it detaches role policies from the user that it detected. 
