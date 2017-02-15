from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Projects"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Project",
					"description": _("Project master."),
				},
				{
					"type": "doctype",
					"name": "Task",
					"description": _("Project activity / task."),
				},
			]
		},
		{
			"label": _("Time Tracking"),
			"items": [
				{
					"type": "doctype",
					"name": "Timesheet",
					"description": _("Timesheet for tasks."),
				},
				{
					"type": "doctype",
					"name": "Activity Type",
					"description": _("Types of activities for Time Logs"),
				},
				{
					"type": "doctype",
					"name": "Activity Cost",
					"description": _("Cost of various activities"),
				},
			]
		},
		{
			"label": _("Help"),
			"icon": "icon-facetime-video",
			"items": [
				{
					"type": "help",
					"label": _("Managing Projects"),
					"youtube_id": "egxIGwtoKI4"
				},
			]
		},
	]
