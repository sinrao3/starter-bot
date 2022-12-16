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
    #print(payload_dict)
    #views related to model
    if(payload_dict.get('view') != None and (payload_dict.get('view').get('title').get('text')== "Wormly downtimes")):
        if(payload_dict.get('type')=="block_actions"):
            block_ids=[]
            selected_values = []
            blocks = payload_dict.get('view').get('blocks')
            view_id=payload_dict.get('view').get('root_view_id')
            for block in blocks:
                block_id = block.get('block_id')
                block_ids.append(block_id)
            for block_id in block_ids[:-2]:
                selected_value = payload_dict.get('view').get('state').get('values').get(block_id).get('plain_text_input-action').get('value')
                selected_values.append(selected_value)
            print(selected_values)
            if(payload_dict.get('view').get('state').get('values').get(block_ids[4]) != None):
                selected_values.append(payload_dict.get('view').get('state').get('values').get(block_ids[4]).get('radio_buttons-action').get('selected_option').get('text').get('text'))
            else:
                string_data=payload_dict.get('view').get('blocks')[4].get('text').get('text')
                selected_values.append(string_data[-5:])
            print(selected_values)
            view=maintenance_utility.maintenance_utility_Schedule_all_wormly_downtime(selected_values)
            client.views_update(token = token, view = view, view_id=view_id)
    #views related to blocks and opening views
    else:
        trigger_id = payload_dict.get('trigger_id')
        channel_id = payload_dict.get('container').get('channel_id')
        ts=payload_dict.get('container').get('message_ts')
        if(payload_dict.get('message').get('text')== "Select synthetic test ID"):
            selected_options=payload_dict.get('actions')[0].get('selected_options')
            options=[]
            for option in selected_options:
                options.append(option.get('text').get('text'))
            if(payload_dict.get('message').get('blocks')[0].get('accessory').get('placeholder').get('text')=='Pause IDs'):
                blocks=maintenance_utility.do_Pause_by_ID(config,options)
            else:
                blocks=maintenance_utility.do_Unpause_by_ID(config,options)
            client.chat_postMessage(channel = channel_id, blocks=blocks)
        elif(payload_dict.get('message').get('text')== "Select a wormly host ID"):
            selected_hostID=payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
            blocks=maintenance_utility.get_wormly_downtimes_by_hostID(selected_hostID)
            client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks)
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
