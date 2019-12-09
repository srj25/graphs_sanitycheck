import boto3
import sys
import datetime
import ast
import json

rule_name = 'shreyatocheck'
# # scheduleExpression = ast.literal_eval(input_json)['scheduleExpression']
client = boto3.client('events', region_name='us-east-1')
# scheduleExpressionCRON = "cron(0/1 * 1/1 * ? *)"
# client.put_rule(Name=rule_name, ScheduleExpression=scheduleExpressionCRON, State='ENABLED')
# print("Rule Created")

response = client.delete_rule(
    Name=rule_name,
    Force=True
)
print("Rule Deleted")