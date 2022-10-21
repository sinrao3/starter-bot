from inspect import BlockFinder
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import maintenance_automation
import json


env_path=Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app=Flask(__name__)
#slack_event_adapter=SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
#BOT_ID=client.api_call("auth.test")['user_id']

# @slack_event_adapter.on('message')
# def message(payload):
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = event.get('text')

#     if BOT_ID != user_id:
#         client.chat_postMessage(channel=channel_id, text=text)


@app.route('/start', methods=['POST'])
def start():
    data=request.form
    channel_id = data.get('channel_id')
    blocks=maintenance_automation.main_menu()
    client.chat_postMessage(channel=channel_id, blocks=blocks)
    return Response(), 200

@ app.route('/result', methods=['POST'])
def menu():
    data = request.form
    payload = data.get('payload')
    payload_dict = json.loads(payload)
    print(payload_dict)
    channel_id = payload_dict.get('container').get('channel_id')
    selected_option = payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
    selected_value=payload_dict.get('actions')[0].get('selected_option').get('value')
    token=os.environ['SLACK_TOKEN']
    ts=payload_dict.get('container').get('message_ts')
    blocks=maintenance_automation.selected_from_main_menu(selected_option)
    client.chat_update(token=token,channel = channel_id,ts=ts, blocks=blocks)
    return Response(), 200


if __name__ == "__main__":
    app.run(debug=True,port=5001)
