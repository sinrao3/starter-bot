import maintenance_utility
my_modal_list=["Schedule_all_wormly_downtimes", "View_scheduled_maintenances"]

my_modal_titles={"Wormly downtimes":"Schedule_all_wormly_downtime",
"Zabbix maintenances":"Zabbix_maintenances",
"Host ID for hk":"Host_IDs",
"Host ID for th":"Host_IDs",
"Maint. ID for hk":"View_scheduled_maintenances",
"Maint. ID for hk":"View_scheduled_maintenances",
"View maint.":"View_scheduled_maintenances"}

def header_blocks():
	blocks=	[
        {
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "MAINTENANCE/DOWNTIME UTILITY"
			}
		}
    ]
	return blocks

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
				"placeholder": {
					"type": "plain_text",
					"text": "YYYY-MM-DDTHH:MM:SS,YYYY-MM-DDTHH:MM:SS"
    			},
				"dispatch_action_config": {
      				"trigger_actions_on": ["on_enter_pressed"]
    			}
			},
			"label": {
				"type": "plain_text",
				"text": "Enter start and end date and time"
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
							"text": "Schedule wormly downtime for hostID"
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
	
def option_Schedule_all_wormly_downtimes():
	results=maintenance_utility.get_default_wormly_downtimes()
	view= {
		"type": "modal",
		"title": {
			"type": "plain_text",
			"text": "Wormly downtimes",
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
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[0]
				},
				"label": {
					"type": "plain_text",
					"text": "Date for downtime (YYYY-MM-DD)",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[1]
				},
				"label": {
					"type": "plain_text",
					"text": "Start time for downtime(HH:MM)",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[2]
				},
				"label": {
					"type": "plain_text",
					"text": "End time for downtime (HH:MM)",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[3]
				},
				"label": {
					"type": "plain_text",
					"text": "Timezone",
					"emoji": True
				}
			},
			{
			"type": "input",
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "MyJS",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "CFS",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Both",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "radio_buttons-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Set downtimes for",
				"emoji": True
			}
		},
		{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Click the button to schedule downtime"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Schedule",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action"
                }
            }
		]
	}
	return view

def option_Schedule_wormly_downtime_for_hostID(results,selected_hostID):
	view= {
		"type": "modal",
		"title": {
			"type": "plain_text",
			"text": "Wormly downtimes",
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
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[0]
				},
				"label": {
					"type": "plain_text",
					"text": "Date for downtime (YYYY-MM-DD)",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[1]
				},
				"label": {
					"type": "plain_text",
					"text": "Start time for downtime(HH:MM)",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[2]
				},
				"label": {
					"type": "plain_text",
					"text": "End time for downtime (HH:MM)",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action",
					"initial_value":results[3]
				},
				"label": {
					"type": "plain_text",
					"text": "Timezone",
					"emoji": True
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": "The selected wormly hostID is: " + selected_hostID,
					"emoji": True
				}
			},
			{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Click the button to schedule downtime"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Schedule",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action"
                }
            }
		]
	}
	return view

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
	view= {
		"type": "modal",
		"title": {
			"type": "plain_text",
			"text": "Zabbix maintenances",
			"emoji": True
		},
		"submit": {
			"type": "plain_text",
			"text": "Submit",
			"emoji": True
		},
		"close": {
			"type": "plain_text",
			"text": "Cancel",
			"emoji": True
		},
		"blocks": [
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action"
				},
				"label": {
					"type": "plain_text",
					"text": "Please type in hk for Hongkong and th for Thailand",
					"emoji": True
				}
			},
			{
				"type": "input",
				"element": {
					"type": "plain_text_input",
					"action_id": "plain_text_input-action"
				},
				"label": {
					"type": "plain_text",
					"text": "Please type in 0 for Host ID and 1 for Maintenance ID",
					"emoji": True
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Click next to continue"
				},
				"accessory": {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Click Me",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "button-action"
				}
			}
		]
	}
	return view
# def option_View_scheduled_maintenances():
# 	blocks = [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Pick a View scheduled maintenance option from the list"
# 			},
# 			"accessory": {
# 				"type": "static_select",
# 				"placeholder": {
# 					"type": "plain_text",
# 					"text": "Select"
# 				},
# 				"options":[
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "View scheduled maintenance for hongkong"
# 						},
# 						"value": "0"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "View scheduled maintenance for thailand"
# 						},
# 						"value": "1"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Quit"
# 						},
# 						"value": "2"
# 					}
# 				],
# 				"action_id": "static_select-action"
# 			}
# 		}
# 	]
# 	return blocks

# def option_View_scheduled_maintenance_for_hongkong():
# 	blocks = [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Pick Host ID or Maintenance ID option from the list"
# 			},
# 			"accessory": {
# 				"type": "static_select",
# 				"placeholder": {
# 					"type": "plain_text",
# 					"text": "Select"
# 				},
# 				"options":[
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Viewing hk maintenances for a host ID"
# 						},
# 						"value": "0"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Viewing hk maintenance for maintenance ID"
# 						},
# 						"value": "1"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Quit"
# 						},
# 						"value": "2"
# 					}
# 				],
# 				"action_id": "static_select-action"
# 			}
# 		}
# 	]
# 	return blocks

# def option_View_scheduled_maintenance_for_thailand():
# 	blocks = [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Pick Host ID or Maintenance ID option from the list"
# 			},
# 			"accessory": {
# 				"type": "static_select",
# 				"placeholder": {
# 					"type": "plain_text",
# 					"text": "Select"
# 				},
# 				"options":[
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Viewing th maintenance for a host ID"
# 						},
# 						"value": "0"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Viewing th maintenance for maintenance ID"
# 						},
# 						"value": "1"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Quit"
# 						},
# 						"value": "2"
# 					}
# 				],
# 				"action_id": "static_select-action"
# 			}
# 		}
# 	]
# 	return blocks

# def option_Viewing_hk_maintenances_for_a_host_ID():
# 	blocks = [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Pick Server option from the list"
# 			},
# 			"accessory": {
# 				"type": "static_select",
# 				"placeholder": {
# 					"type": "plain_text",
# 					"text": "Select"
# 				},
# 				"options":[
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Web Server"
# 						},
# 						"value": "0"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Agent Server"
# 						},
# 						"value": "1"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Relinquish Server"
# 						},
# 						"value": "2"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Quit"
# 						},
# 						"value": "3"
# 					}
# 				],
# 				"action_id": "static_select-action"
# 			}
# 		}
# 	]
# 	return blocks

# def option_Viewing_hk_maintenances_for_maintenance_ID():
# 	blocks = [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Pick Server option from the list"
# 			},
# 			"accessory": {
# 				"type": "static_select",
# 				"placeholder": {
# 					"type": "plain_text",
# 					"text": "Select"
# 				},
# 				"options":[
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Web Server"
# 						},
# 						"value": "0"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Agent Server"
# 						},
# 						"value": "1"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Relinquish Server"
# 						},
# 						"value": "2"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Quit"
# 						},
# 						"value": "3"
# 					}
# 				],
# 				"action_id": "static_select-action"
# 			}
# 		}
# 	]
# 	return blocks

# def option_Viewing_th_maintenances_for_a_host_ID():
# 	blocks = [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Pick Server option from the list"
# 			},
# 			"accessory": {
# 				"type": "static_select",
# 				"placeholder": {
# 					"type": "plain_text",
# 					"text": "Select"
# 				},
# 				"options":[
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Web Server"
# 						},
# 						"value": "0"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Agent Server"
# 						},
# 						"value": "1"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Relinquish Server"
# 						},
# 						"value": "2"
# 					},
# 					{
# 						"text": {
# 							"type": "plain_text",
# 							"text": "Quit"
# 						},
# 						"value": "3"
# 					}
# 				],
# 				"action_id": "static_select-action"
# 			}
# 		}
# 	]
# 	return blocks

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

