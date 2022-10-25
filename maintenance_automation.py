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
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "The "+ selected_menu+ "option you selected is  *" + selected_option +"*"
			}
		}
	]
	return blocks

def option_DataDog():
	blocks = [
		{
			"type": "divider"
		},
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
							"text": "Synthetic Tests "
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

