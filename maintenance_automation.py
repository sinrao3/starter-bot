def main_menu():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a maintenance/downtime option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Banner"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Cloudflare/Pages"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "DataDog"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wormly"
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Zabbix"
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "5"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def selected_from_menu(selected_option,selected_menu):
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "The "+ selected_menu+ " option you selected is  *" + selected_option +"*"
			}
		},
		{
			"type": "divider"
		}
	]
	return blocks

def option_Back_to_Main_Menu():
	return main_menu()
   
def option_Quit():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*You have stopped the maintenance bot*"
			}
		}
	]
	return blocks

#Datadog
def option_DataDog():
	blocks = [
		
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a DataDog option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Synthetic tests"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Datadog downtimes"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "3"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Synthetic_tests():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Synthetic tests option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Get all"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Get by status"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Pause all"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Unpause all"
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Pause by ID"
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Unpause by ID"
						},
						"value": "5"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "6"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "7"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Get_by_status():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Get by status option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select"
				},
				"options":[
					{
						"text": {
							"type": "plain_text",
							"text": "Get by status Live"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Get by status Paused"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "2"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Datadog_downtimes():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Downtimes option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Get all datadog downtimes"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Get datadog downtimes by status"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule datadog downtime"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "4"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Get_datadog_downtimes_by_status():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Get datdog downtimes by status option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select"
				},
				"options":[
					{
						"text": {
							"type": "plain_text",
							"text": "Get datadog downtimes by status Live"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Get datadog downtimes by status Scheduled"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "2"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Schedule_datadog_downtime():
	blocks= [
		{
			"type": "input",
			"dispatch_action": True,
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action",
				"dispatch_action_config": {
      				"trigger_actions_on": ["on_enter_pressed"]
    			}
			},
			"label": {
				"type": "plain_text",
				"text": "Enter start and end date and time (YYYY-MM-DDTHH:MM:SS,YYYY-MM-DDTHH:MM:SS)"
			}
		}
	]
	return blocks

#Wormly
def option_Wormly():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Wormly option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Get all wormly downtimes"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Get wormly downtimes by hostID"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule all wormly downtimes"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule wormly downtime for HostID"
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "5"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Get_all_wormly_downtimes():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Get all wormly downtimes option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "MyJS"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "CFS"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Both"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "3"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks
	
# def Get_wormly_downtimes_by_hostID():
# def Schedule_all_wormly_downtimes():
# def Schedule_wormly_downtime_for_hostID():
#Zabbix
def option_Zabbix():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Zabbix option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "View scheduled maintenances"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule zabbix downtime"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Delete maintenance"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to Main Menu"
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "4"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_View_scheduled_maintenances():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a View scheduled maintenance option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select"
				},
				"options":[
					{
						"text": {
							"type": "plain_text",
							"text": "View scheduled maintenance for hongkong"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "View scheduled maintenance for thailand"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "2"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

def option_Schedule_zabbix_downtime():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Schedule downtime option from the list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select"
				},
				"options":[
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule downtime for hongkong"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule downtime for thailand"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Quit"
						},
						"value": "2"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
	return blocks

