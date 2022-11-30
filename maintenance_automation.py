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
							"text": "Synthetic Tests"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Downtimes"
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

def option_Synthetic_Tests():
	blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a Synthetic Tests option from the list"
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
							"text": "Un-pause all"
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
							"text": "Un-pause by ID"
						},
						"value": "5"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to main menu"
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

def option_Downtimes():
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
							"text": "Schedule"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Cancel"
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to main menu"
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
							"text": "Live"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Paused"
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
							"text": "View Scheduled Maintenances"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Schedule Downtime"
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Delete Maintenance"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Back to main menu"
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

def option_View_Scheduled_Maintenances():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a View Scheduled Maintenance option from the list"
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
							"text": "Hongkong"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thailand"
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

def option_Schedule_Downtime():
	blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a View Scheduled Maintenance option from the list"
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
							"text": "Hongkong"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thailand"
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