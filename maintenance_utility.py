import mtools
import datetime
my_list =["Get_all","Get_by_status_Live","Get_by_status_Paused","Pause_all","Unpause_all","Pause_by_ID","Unpause_by_ID","Get_all_datadog_downtimes",
"Get_datadog_downtimes_by_status_Live","Get_datadog_downtimes_by_status_Scheduled","MyJS","CFS","Both","Get_wormly_downtimes_by_hostID","Schedule_wormly_downtime_for_hostID"] 

my_dict={
	"Select synthetic test ID to pause" :"do_Pause_by_ID",
	"Select synthetic test ID to unpause": "do_Unpause_by_ID",
	"Enter start and end date and time" : "maintenance_utility_Schedule_datadog_downtime",
	"Select a wormly host ID" : "get_wormly_downtimes_by_hostID"
}
#***********Synthetic tests start***********
#Datadog->Synthetic tests->Get all
def maintenance_utility_Get_all(config):
	synthetic_tests=mtools.list_synthetic_tests(config, 'all', False)
	blocks=create_block(synthetic_tests)
	return blocks

#Datadog->Synthetic tests->Get by status->Get by status Live
def maintenance_utility_Get_by_status_Live(config):
	synthetic_tests=mtools.list_synthetic_tests(config, 'live', False)
	blocks=create_block(synthetic_tests)
	return blocks

#Datadog->Synthetic tests->Get by status->Get by status Paused
def maintenance_utility_Get_by_status_Paused(config):
	synthetic_tests=mtools.list_synthetic_tests(config, 'paused', False)
	blocks=create_block(synthetic_tests)
	return blocks

#Datadog->Synthetic tests->Pause all
def maintenance_utility_Pause_all(config):
	synthetic_tests_pause_unpause=mtools.pause_unpause_all_synthetic_tests(config, 'paused')
	blocks=create_block(synthetic_tests_pause_unpause)
	return blocks

#Datadog->Synthetic tests->Unpause all
def maintenance_utility_Unpause_all(config):
	synthetic_tests_pause_unpause=mtools.pause_unpause_all_synthetic_tests(config, 'live')
	blocks=create_block(synthetic_tests_pause_unpause)
	return blocks

#Datadog->Synthetic tests->Pause by ID
def maintenance_utility_Pause_by_ID(config):
	list=mtools.list_synthetic_tests(config, 'all', True)
	options=create_options_for_multiple_select(list)
	multiple_select_menu=create_multiple_select('Select synthetic test ID to pause','Pause IDs',options)
	return multiple_select_menu

#Datadog->Synthetic tests->Unpause by ID
def maintenance_utility_Unpause_by_ID(config):
	list=mtools.list_synthetic_tests(config, 'all', True)
	options=create_options_for_multiple_select(list)
	multiple_select_menu=create_multiple_select('Select synthetic test ID to unpause','Unpause IDs',options)
	return multiple_select_menu

#Datadog->Synthetic tests->Pause by ID->Multi-static-select for IDs
def do_Pause_by_ID(config,payload_dict):
	selected_options=payload_dict.get('actions')[0].get('selected_options')
	options=[]
	for option in selected_options:
		options.append(option.get('text').get('text'))
	synthetic_tests_pause_unpause=mtools.pause_unpause_synthetic_tests(config, options, 'paused')
	blocks=create_block(synthetic_tests_pause_unpause)
	return blocks

#Datadog->Synthetic tests->Pause by ID->Multi-static-select for IDs
def do_Unpause_by_ID(config,payload_dict):
	selected_options=payload_dict.get('actions')[0].get('selected_options')
	options=[]
	for option in selected_options:
		options.append(option.get('text').get('text'))
	synthetic_tests_pause_unpause=mtools.pause_unpause_synthetic_tests(config, options, 'live')
	blocks=create_block(synthetic_tests_pause_unpause)
	return blocks

#***********Synthetic tests end***********

#***********Datadog downtime start***********

#Datadog->Datdog downtimes->Get all datadog downtimes
def maintenance_utility_Get_all_datadog_downtimes(config):
	downtimes=mtools.list_downtimes(config, "all")
	blocks=create_block(downtimes)
	return blocks

#Datadog->Datadog downtimes->Get datadog downtimes by status->Get datadog downtimes by status Live
def maintenance_utility_Get_datadog_downtimes_by_status_Live(config):
	downtimes=mtools.list_downtimes(config, "live")
	blocks=create_block(downtimes)
	return blocks

#Datadog->Datadog downtimes->Get datadog downtimes by status->Get datadog downtimes by status Paused
def maintenance_utility_Get_datadog_downtimes_by_status_Scheduled(config):
	downtimes=mtools.list_downtimes(config, "scheduled")
	blocks=create_block(downtimes)
	return blocks

#Datadog->Datadog downtimes->Schedule datadog downtime
#To-do----->make model
def maintenance_utility_Schedule_datadog_downtime(config,payload_dict):
	selected_value=payload_dict.get('actions')[0].get('value')
	start_end = selected_value.split(',')
	start_dt = start_end[0].split('T')
	start_dp = start_dt[0].split('-')
	start_tp = start_dt[1].split(':')
	end_dt = start_end[1].split('T')
	end_dp = end_dt[0].split('-')
	end_tp = end_dt[1].split(':')

	# Schedule a Downtime
	downtime_start_datetime = datetime.datetime(int(start_dp[0]), int(start_dp[1]),
										int(start_dp[2]), int(start_tp[0]),
										int(start_tp[1]), int(start_tp[2]))

	downtime_end_datetime = datetime.datetime(int(end_dp[0]), int(end_dp[1]),
										int(end_dp[2]), int(end_tp[0]),
										int(end_tp[1]), int(end_tp[2]))

	# Get the POSIX timestamp values
	downtime_start = int(downtime_start_datetime.timestamp())
	downtime_end = int(downtime_end_datetime.timestamp())
	downtimes=mtools.schedule_downtime(config, downtime_start, downtime_end)
	blocks=create_block(downtimes)
	return blocks
#***********Downtime end***********

#***********Wormly start***********
#Wormly->Get all wormly downtimes->MyJS
def maintenance_utility_MyJS(config):
	blocks=mtools.get_wormly_downtimes(mtools.myjs_hostids, False)
	return blocks

#Wormly->Get all wormly downtimes->CFS
def maintenance_utility_CFS(config):
	blocks=mtools.get_wormly_downtimes(mtools.cfs_hostids, False)
	return blocks

#Wormly->Get all wormly downtimes->Both
def maintenance_utility_Both(config):
	blocks=mtools.get_wormly_downtimes(mtools.myjs_hostids+mtools.cfs_hostids, False)
	return blocks

#Wormly->Get wormly downtimes by hostID
def maintenance_utility_Get_wormly_downtimes_by_hostID(config):
	options=[]
	j=0
	for i in mtools.myjs_hostids:
		option={
					"text": {
						"type": "plain_text",
						"text": i,
						"emoji": True
					},
					"value": "value-"+str(j)
				}
		options.append(option)
		j+=1
	for i in mtools.cfs_hostids:
		option={
					"text": {
						"type": "plain_text",
						"text": i,
						"emoji": True
					},
					"value": "value-"+str(j)
				}
		options.append(option)
		j+=1
	blocks=create_static_select(options,"Select a wormly host ID")
	return blocks

#Wormly->Get wormly downtimes by hostID->hostID
def get_wormly_downtimes_by_hostID(config,payload_dict):
	selected_hostID=payload_dict.get('actions')[0].get('selected_option').get('text').get('text')
	blocks=mtools.get_wormly_downtimes([selected_hostID], False)
	return blocks
	
#To get default values while Scheduling downtimes
def get_default_wormly_downtimes(selected_hostID=mtools.myjs_hostids[0]):
	result=mtools.get_wormly_downtimes([selected_hostID], True)
	results=[]
	results.append(result[0][selected_hostID]['on'])
	results.append(result[0][selected_hostID]['start'])
	results.append(result[0][selected_hostID]['end'])
	results.append(result[0][selected_hostID]['timezone'])
	return results

#Wormly->Schedule all wormly downtimes
def maintenance_utility_Schedule_all_wormly_downtime(payload_dict):
	block_ids=[]
	selected_values = []
	blocks = payload_dict.get('view').get('blocks')
	for block in blocks:
		block_id = block.get('block_id')
		block_ids.append(block_id)
	for block_id in block_ids[:-2]:
		selected_value = payload_dict.get('view').get('state').get('values').get(block_id).get('plain_text_input-action').get('value')
		selected_values.append(selected_value)
	if(payload_dict.get('view').get('state').get('values').get(block_ids[4]) != None):
		selected_values.append(payload_dict.get('view').get('state').get('values').get(block_ids[4]).get('radio_buttons-action').get('selected_option').get('text').get('text'))
	else:
		string_data=payload_dict.get('view').get('blocks')[4].get('text').get('text')
		selected_values.append(string_data[-5:])

	if(selected_values[4]=="MyJS"):
		views=mtools.set_wormly_downtimes(mtools.myjs_hostids, selected_values[1], selected_values[2], selected_values[3], "ONCEONLY",selected_values[0])
	elif(selected_values[4]=="CFS"):
		views=mtools.set_wormly_downtimes(mtools.cfs_hostids, selected_values[1], selected_values[2], selected_values[3], "ONCEONLY",selected_values[0])
	elif(selected_values[4]=="Both"):
		views=mtools.set_wormly_downtimes(mtools.myjs_hostids+mtools.cfs_hostids, selected_values[1], selected_values[2], selected_values[3], "ONCEONLY",selected_values[0])
	else:
		views=mtools.set_wormly_downtimes([selected_values[4]], selected_values[1], selected_values[2], selected_values[3], "ONCEONLY",selected_values[0])
	return views

#Wormly->Schedule wormly downtimes for hostID
def maintenance_utility_Schedule_wormly_downtime_for_hostID(config):
	options=create_options_for_multiple_select(mtools.myjs_hostids+mtools.cfs_hostids)
	blocks=create_static_select(options,"Select a wormly hostID")
	return blocks

#***********Wormly end***********
def create_block(data):
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": data
			}
		},
		{
			"type": "divider"
		}
	]
	return blocks    

def create_modal(title,data):
	views= {
		"type": "modal",
		"title": {
			"type": "plain_text",
			"text": title,
			"emoji": True
		},
		"submit": {
			"type": "plain_text",
			"text": "Done",
			"emoji": True
		},
		"close": {
			"type": "plain_text",
			"text": "Cancel",
			"emoji": True
		},
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": data,
					"emoji": True
				}
			}
		]
	}
	return views

def create_multiple_select(text,title,options):
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": text
			},
			"accessory":{
				"type": "multi_static_select",
				"placeholder": {
					"type": "plain_text",
					"text": title,
					"emoji": True
				},
				"options":options,
				"action_id": "multi_static_select-action"
			}
		}
	]
	return blocks

def create_static_select(options,text):
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": text
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": options,
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def create_options_for_multiple_select(list):
	options=[]
	j=0
	for i in list:
		option={
					"text": {
						"type": "plain_text",
						"text": i,
						"emoji": True
					},
					"value": "value-"+str(j)
				}
		options.append(option)
		j+=1
	return options

