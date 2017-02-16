from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Sales"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Quotation",
					"description": _("Quotes to Leads or Customers."),
				},
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Confirmed orders from Customers."),
				},
				{
					"type": "doctype",
					"name": "Call Log",
					"description": _("Call Log")
				},
				{
					"type": "doctype",
					"name": "Daily Route Activity",
					"description": _("Daily Route Activity."),
				},
				{
					"type": "doctype",
					"name": "Outlet Survey",
					"description": _("Outlet Survey."),
				},
				{
					"type": "doctype",
					"name": "Performance Assessment Form",
					"description": _("Performance Assessment Form."),
				},
				{
					"type": "doctype",
					"name": "Authority to Load",
					"description": _("Create a new authority to load from sales order"),
				}
			]
		},
		{
			"label": _("Customers"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"label": _("Customer Group"),
					"name": "Customer Group",
					"icon": "icon-sitemap",
					"link": "Tree/Customer Group",
					"description": _("Manage Customer Group Tree."),
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("All Addresses."),
				},

			]
		},
		{
			"label": _("Items and Pricing"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("All Products or Services."),
				},
				{
					"type": "doctype",
					"name": "Product Bundle",
					"description": _("Bundle items at time of sale."),
				},
				{
					"type": "doctype",
					"name": "Price List",
					"description": _("Price List master.")
				},
				{
					"type": "doctype",
					"name": "Item Group",
					"icon": "icon-sitemap",
					"label": _("Item Group"),
					"link": "Tree/Item Group",
					"description": _("Tree of Item Groups."),
				},
				{
					"type": "doctype",
					"name": "Item Price",
					"description": _("Multiple Item prices."),
					"route": "Report/Item Price"
				},
				{
					"type": "doctype",
					"name": "Shipping Rule",
					"description": _("Rules for adding shipping costs.")
				},
				{
					"type": "doctype",
					"name": "Pricing Rule",
					"description": _("Rules for applying pricing and discount.")
				},

			]
		},
		{
			"label": _("Sales Partners and Territory"),
			"items": [
				{
					"type": "doctype",
					"label": _("Territory"),
					"name": "Territory",
					"icon": "icon-sitemap",
					"link": "Tree/Territory",
					"description": _("Manage Territory Tree."),
				},
				{
					"type": "doctype",
					"name": "Sales Partner",
					"description": _("Manage Sales Partners."),
				},
				{
					"type": "doctype",
					"label": _("Sales Person"),
					"name": "Sales Person",
					"icon": "icon-sitemap",
					"link": "Tree/Sales Person",
					"description": _("Manage Sales Person Tree."),
				},
				
			]
		},
		{
			"label": _("Setup"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Selling Settings",
					"description": _("Default settings for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "Campaign",
					"description": _("Sales campaigns."),
				},
				{
					"type": "doctype",
					"name":"Terms and Conditions",
					"label": _("Terms and Conditions Template"),
					"description": _("Template of terms or contract.")
				},
				{
					"type": "doctype",
					"name": "Sales Taxes and Charges Template",
					"description": _("Tax template for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "Industry Type",
					"description": _("Track Leads by Industry Type.")
				},
				{
					"type": "doctype",
					"name": "Visit Status",
					"description": "Visit Status",
				},
				{
					"type": "doctype",
					"name": "Outlet Type",
					"description": "Outlet Type",
				},
				{
					"type": "doctype",
					"name": "Competitor",
					"description": "Competitor",
				},
				{
					"type": "doctype",
					"name": "Measurement Variable",
					"description": "Measurement Variable",
				},
			]
		},
		{
			"label": _("SMS"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "SMS Center",
					"description":_("Send mass SMS to your contacts"),
				},
				{
					"type": "doctype",
					"name": "SMS Log",
					"description":_("Logs for maintaining sms delivery status"),
				},
				{
					"type": "doctype",
					"name": "SMS Settings",
					"description": _("Setup SMS gateway settings")
				},
			]
		},
		{
			"label": _("Help"),
			"items": [
				{
					"type": "help",
					"label": _("Customer and Supplier"),
					"youtube_id": "anoGi_RpQ20"
				},
				{
					"type": "help",
					"label": _("Sales Order to Payment"),
					"youtube_id": "7AMq4lqkN4A"
				},
				{
					"type": "help",
					"label": _("Point-of-Sale"),
					"youtube_id": "4WkelWkbP_c"
				},
			]
		},
	]
