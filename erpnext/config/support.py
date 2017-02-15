from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
                {
                        "label": _("Helpdesk"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Helpdesk Ticket",
                                        "description": _("Helpdesk Ticket."),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Job Card",
                                        "description": _("Job Card."),
                                },
                        ]
                },
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Issue",
					"description": _("Support queries from customers."),
				},
				{
					"type": "doctype",
					"name": "Communication",
					"description": _("Communication log."),
				},
				{
					"type": "doctype",
					"name": "Computing Asset Inspection Checklist"
				},
				{
					"type": "doctype",
					"name": "Generator Fuel Consumption Log"
				},
				{
					"type": "doctype",
					"name": "Daily Generator Activity Log"
				},
				{
					"type": "doctype",
					"name": "Fixed Asset Inspection Checklist"
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Computing Asset Type"
				},
				{
					"type": "doctype",
					"name": " Computing Asset Inspection Status"
				},
				{
					"type": "doctype",
					"name": "Fixed Asset Inspection Status"
				},
			]
		},
		{
			"label": _("Warranty"),
			"items": [
				{
					"type": "doctype",
					"name": "Warranty Claim",
					"description": _("Warranty Claim against Serial No."),
				},
				{
					"type": "doctype",
					"name": "Serial No",
					"description": _("Single unit of an Item."),
				},
			]
		},
                {
                        "label": _("Setup"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Request Type",
                                        "description": _("Request Type."),
                                },
                        ]
                },
	]
