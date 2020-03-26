# slack-exporter
Python scripts to export slack data

# Introduction

A set of scripts to extract data from slack to CSV. This is being used for Romsey Mutual Aid, an organization created to help people in Romsey, Cambridge, UK.

# Install
It is a Python 3 app. I recommend you to use Python's virtual environment. To install packages you need to run `pip3 install -r requirements.txt`

You will need to setup an Environment varialble for the slack API key:
`export SLACK_API_TOKEN=insert_slack_api_token`

In slack you should create one app and allow it to user:read

# Run

`python3 extract_from_slack.py`

This command will export the list of users to `data/slack_users.csv`

