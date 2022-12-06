import mtools

my_list =["Get_all","Get_by_status_Live","Get_by_status_Paused","Pause_all","Unpause_all","Pause_by_ID","Unpause_by_ID"] 

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

