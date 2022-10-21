def main_menu():
	blocks = [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "MAINTENANCE/DOWNTIME UTILITY"
			}
		},
		{
			"type": "divider"
		},
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

def selected_from_main_menu(selected_option):
	blocks= [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "The maintenance/automation option you selected is  *" + selected_option +"*"
			}
		}
	]
	return blocks
