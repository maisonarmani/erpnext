// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Purchase Order"] = {
	field_map: {
		"start": "schedule_date",
		"end": "schedule_date",
		"id": "name",
		"title": "name",
		"allDay": "allDay"
	},
	gantt: true,
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "supplier",
			"options": "Supplier",
			"label": __("Supplier")
		},
	],
	get_events_method: "erpnext.buying.doctype.purchase_order.purchase_order.get_events"
}

