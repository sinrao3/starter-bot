from inspect import BlockFinder
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import maintenance_automation
import json

selected_menu="maintenance/automation"

env_path=Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app=Flask(__name__)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

@app.route('/start', methods=['POST'])
def start():
    data=request.form
    channel_id = data.get('channel_id')
    header_blocks=	[
        {
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "MAINTENANCE/DOWNTIME UTILITY"
			}
		}
        ]
    client.chat_postMessage(channel=channel_id, blocks=header_blocks)
    blocks=maintenance_automation.main_menu()
    client.chat_postMessage(channel=channel_id, blocks=blocks)
    return Response(), 200


@ app.route('/result', methods=['POST'])
def result():
    global selected_menu
    data = request.form
    payload = data.get('payload')
    payload_dict = json.loads(payload)
    channel_id = payload_dict.get('container').get('channel_id')
    selected_option = payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
    selected_value=payload_dict.get('actions')[0].get('selected_option').get('value')
    token=os.environ['SLACK_TOKEN']
    ts=payload_dict.get('container').get('message_ts')
    blocks=maintenance_automation.selected_from_menu(selected_option,selected_menu)
    selected_menu=selected_option
    selected_option=selected_option.replace(' ', '_')
    client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks)
    blocks1=getattr(maintenance_automation, 'option_%s' % selected_option)()
    client.chat_postMessage(channel = channel_id, blocks=blocks1)
    return Response(), 200


if __name__ == "__main__":
    app.run(debug=True,port=5001)
