from inspect import BlockFinder
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import maintenance_automation
import maintenance_utility
import json
from datadog_api_client.v1 import Configuration

selected_menu="maintenance/automation"
env_file = os.path.dirname(os.path.realpath(__file__)) + os.sep + "config/env.file"
load_dotenv(env_file)
config= Configuration()

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
    token=os.environ['SLACK_TOKEN']
    ts=payload_dict.get('container').get('message_ts')
    if(payload_dict.get('actions')[0].get('type')== 'multi_static_select'):
        selected_options=payload_dict.get('actions')[0].get('selected_options')
        options=[]
        for option in selected_options:
            options.append(option.get('text').get('text'))
        if(payload_dict.get('message').get('blocks')[0].get('accessory').get('placeholder').get('text')=='Pause IDs'):
            blocks=maintenance_utility.do_Pause_by_ID(config,options)
        else:
            blocks=maintenance_utility.do_Unpause_by_ID(config,options)
        client.chat_postMessage(channel = channel_id, blocks=blocks)
    elif(payload_dict.get('actions')[0].get('type')== 'plain_text_input'):
        selected_value=payload_dict.get('actions')[0].get('value')
        blocks3=maintenance_utility.maintenance_utility_Schedule_datadog_downtime(config,selected_value)
        client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks3)
    else:
        selected_option = payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
        blocks=maintenance_automation.selected_from_menu(selected_option,selected_menu)
        selected_menu=selected_option
        selected_option=selected_option.replace(' ', '_')
        client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks)
        if selected_option in maintenance_utility.my_list:
            blocks1=getattr(maintenance_utility,'maintenance_utility_%s' % selected_option)(config) 
            client.chat_postMessage(channel = channel_id, blocks=blocks1)   
        else:
            blocks2=getattr(maintenance_automation, 'option_%s' % selected_option)()
            client.chat_postMessage(channel = channel_id, blocks=blocks2)
    return Response(), 200

    
if __name__ == "__main__":
    app.run(debug=True,port=5001)
