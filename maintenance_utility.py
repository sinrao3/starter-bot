import mtools
import datetime
my_list =["Get_all","Get_by_status_Live","Get_by_status_Paused","Pause_all","Unpause_all","Pause_by_ID","Unpause_by_ID","Get_all_datadog_downtimes",
"Get_datadog_downtimes_by_status_Live","Get_datadog_downtimes_by_status_Scheduled","MyJS","CFS","Both"] 

#***********Synthetic tests start***********
def maintenance_utility_Get_all(config):
    blocks=mtools.list_synthetic_tests(config, 'all', False)
    return blocks
    
def maintenance_utility_Get_by_status_Live(config):
	blocks=mtools.list_synthetic_tests(config, 'live', False)
	return blocks

def maintenance_utility_Get_by_status_Paused(config):
	blocks=mtools.list_synthetic_tests(config, 'paused', False)
	return blocks

def maintenance_utility_Pause_all(config):
	blocks=mtools.pause_unpause_all_synthetic_tests(config, 'paused')
	return blocks

def maintenance_utility_Unpause_all(config):
	blocks=mtools.pause_unpause_all_synthetic_tests(config, 'live')
	return blocks

def maintenance_utility_Pause_by_ID(config):
	list=mtools.list_synthetic_tests(config, 'all', True)
	options=create_options_for_multiple_select(list)
	multiple_select_menu=create_multiple_select(options,'Pause IDs')
	return multiple_select_menu

def maintenance_utility_Unpause_by_ID(config):
	list=mtools.list_synthetic_tests(config, 'all', True)
	options=create_options_for_multiple_select(list)
	multiple_select_menu=create_multiple_select(options,'Unpause IDs')
	return multiple_select_menu

def do_Pause_by_ID(config,options):
	blocks=mtools.pause_unpause_synthetic_tests(config, options, 'paused')
	return blocks

def do_Unpause_by_ID(config,options):
	blocks=mtools.pause_unpause_synthetic_tests(config, options, 'live')
	return blocks

#***********Synthetic tests end***********

#***********Datadog downtime start***********
def maintenance_utility_Get_all_datadog_downtimes(config):
	blocks=mtools.list_downtimes(config, "all")
	return blocks

def maintenance_utility_Get_datadog_downtimes_by_status_Live(config):
	blocks=mtools.list_downtimes(config, "live")
	return blocks

def maintenance_utility_Get_datadog_downtimes_by_status_Scheduled(config):
	blocks=mtools.list_downtimes(config, "scheduled")
	return blocks

def maintenance_utility_Schedule_datadog_downtime(config,selected_value):
	start_end = selected_value.split(',')
	print(start_end)
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
	blocks=mtools.schedule_downtime(config, downtime_start, downtime_end)
	return blocks
#***********Downtime end***********

#***********Wormly start***********
def maintenance_utility_MyJS(config):
	blocks=mtools.get_wormly_downtimes(mtools.myjs_hostids, False)
	return blocks

def maintenance_utility_CFS(config):
	blocks=mtools.get_wormly_downtimes(mtools.cfs_hostids, False)
	return blocks

def maintenance_utility_Both(config):
	blocks=mtools.get_wormly_downtimes(mtools.myjs_hostids+mtools.cfs_hostids, False)
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

def create_multiple_select(options,text):
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select Test IDs "
			},
			"accessory":{
				"type": "multi_static_select",
				"placeholder": {
					"type": "plain_text",
					"text": text,
					"emoji": True
				},
				"options":options,
				"action_id": "multi_static_select-action"
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

