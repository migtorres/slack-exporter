import os
import slack
import pdb
import csv
client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
users_list = client.users_list()["members"]

with open('data/slack_users.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Real Name', "Phone", "Title"])
    for user in users_list:
        writer.writerow([user["name"],user["real_name"],user["profile"]["phone"],user["profile"]["title"]])
