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
    header_blocks=maintenance_automation.header_blocks()
    client.chat_postMessage(channel=channel_id, blocks=header_blocks)
    blocks=maintenance_automation.main_menu()
    client.chat_postMessage(channel=channel_id, blocks=blocks)
    return Response(), 200


@ app.route('/result', methods=['POST'])
def result():
    global selected_menu
    token=os.environ['SLACK_TOKEN']
    data = request.form
    payload = data.get('payload')
    payload_dict = json.loads(payload)
    #views related to model updation
    if(payload_dict.get('view') != None and (payload_dict.get('view').get('title').get('text')== "Wormly downtimes")):
        if(payload_dict.get('type')=="block_actions"):
            view_id=payload_dict.get('view').get('root_view_id')
            view=maintenance_utility.maintenance_utility_Schedule_all_wormly_downtime(payload_dict)
            client.views_update(token = token, view = view, view_id=view_id)
            
    #views related to blocks and opening views
    else:
        trigger_id = payload_dict.get('trigger_id')
        channel_id = payload_dict.get('container').get('channel_id')
        ts=payload_dict.get('container').get('message_ts')
        if((message:=maintenance_utility.my_dict.get(payload_dict.get('message').get('text')) )!=None or (payload_dict.get('message').get('blocks')[0].get('label') !=None and (message:=maintenance_utility.my_dict.get(payload_dict.get('message').get('blocks')[0].get('label').get('text'))) !=None) ):
            blocks=getattr(maintenance_utility,message)(config,payload_dict)
            client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks)
        else:
            selected_option = payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
            blocks=maintenance_automation.selected_from_menu(selected_option,selected_menu)
            selected_menu=selected_option
            selected_option=selected_option.replace(' ', '_')
            client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks)
            if(payload_dict.get('message').get('text')== "Select a wormly hostID"):
                selected_hostID=payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
                results=maintenance_utility.get_default_wormly_downtimes(selected_hostID)
                view=maintenance_automation.option_Schedule_wormly_downtime_for_hostID(results,selected_hostID)
                client.views_open(token = token, view = view, trigger_id = trigger_id)
            elif selected_option in maintenance_utility.my_list:
                blocks=getattr(maintenance_utility,'maintenance_utility_%s' % selected_option)(config) 
                client.chat_postMessage(channel = channel_id, blocks=blocks) 
            elif selected_option in maintenance_automation.my_modal_list:
                results=maintenance_utility.get_default_wormly_downtimes()
                view=getattr(maintenance_automation, 'option_%s' % selected_option)(results)
                client.views_open(token = token, view = view, trigger_id = trigger_id)
            else:
                blocks=getattr(maintenance_automation, 'option_%s' % selected_option)()
                client.chat_postMessage(channel = channel_id, blocks=blocks)
    return Response(), 200

    
if __name__ == "__main__":
    app.run(debug=True,port=5001)
