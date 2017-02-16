from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Billing"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("Bills raised to Customers.")
				},
				{
					"type": "doctype",
					"name": "Purchase Invoice",
					"description": _("Bills raised by Suppliers.")
				},
				{
					"type": "doctype",
					"name": "Payment Request",
					"description": _("Payment Request")
				},
				{
					"type": "doctype",
					"name": "Payment Entry",
					"description": _("Bank/Cash transactions against party or for internal transfer")
				},
				{
					"type": "page",
					"name": "pos",
					"label": _("POS"),
					"description": _("Point of Sale")
				},
				{
					"type": "doctype",
					"name": "Payment Voucher Form",
					"description": _("Payment Voucher Form")
				}
				
			]

		},
		{
			"label": _("Company and Accounts"),
			"items": [
				{
					"type": "doctype",
					"name": "Company",
					"description": _("Company (not Customer or Supplier) master.")
				},
				{
					"type": "doctype",
					"name": "Journal Entry",
					"description": _("Accounting journal entries.")
				},
				{
					"type": "doctype",
					"name": "Account",
					"icon": "icon-sitemap",
					"label": _("Chart of Accounts"),
					"route": "Tree/Account",
					"description": _("Tree of financial accounts."),
				},
			]
		},
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database.")
				},
				{
					"type": "doctype",
					"name": "Supplier",
					"description": _("Supplier database.")
				},
				{
					"type": "doctype",
					"name": "Item",
				},
				{
					"type": "doctype",
					"name": "Asset",
				},
				{
					"type": "doctype",
					"name": "Asset Category",
				}
			]
		},
		{
			"label": _("Banking and Payments"),
			"items": [
				{
					"type": "doctype",
					"label": _("Petty Cash Log"),
					"name": "Petty Cash Log",
					"description": _("Petty Cash Log")
				},
				{
					"type": "doctype",
					"label": _("Update Bank Transaction Dates"),
					"name": "Bank Reconciliation",
					"description": _("Update bank payment dates with journals.")
				},
				{
					"type": "doctype",
					"label": _("Match Payments with Invoices"),
					"name": "Payment Reconciliation",
					"description": _("Match non-linked Invoices and Payments.")
				},
			]
		},
		{
			"label": _("Taxes"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Taxes and Charges Template",
					"description": _("Tax template for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "Purchase Taxes and Charges Template",
					"description": _("Tax template for buying transactions.")
				},
				{
					"type": "doctype",
					"name": "Tax Rule",
					"description": _("Tax Rule for transactions.")
				},
			]
		},
		{
			"label": _("Budget and Cost Center"),
			"items": [
				{
					"type": "doctype",
					"name": "Cost Center",
					"icon": "icon-sitemap",
					"label": _("Chart of Cost Centers"),
					"route": "Tree/Cost Center",
					"description": _("Tree of financial Cost Centers."),
				},
				{
					"type": "doctype",
					"name": "Budget",
					"description": _("Define budget for a financial year.")
				},
				{
					"type":"doctype",
					"name": "Monthly Distribution",
					"description": _("Seasonality for setting budgets, targets etc.")
				},
			]
		},
		{
			"label": _("Tools"),
			"items": [
				{
					"type": "doctype",
					"name": "Period Closing Voucher",
					"description": _("Close Balance Sheet and book Profit or Loss.")
				},
				{
					"type": "doctype",
					"name": "Asset Movement",
					"description": _("Transfer an asset from one warehouse to another")
				},
				{
					"type": "doctype",
					"name": "Cheque Print Template",
					"description": _("Setup cheque dimensions for printing")
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Accounts Settings",
					"description": _("Default settings for accounting transactions.")
				},
				{
					"type": "doctype",
					"name": "Fiscal Year",
					"description": _("Financial / accounting year.")
				},
				{
					"type": "doctype",
					"name": "Currency",
					"description": _("Enable / disable currencies.")
				},
				{
					"type": "doctype",
					"name": "Currency Exchange",
					"description": _("Currency exchange rate master.")
				},
				{
					"type": "doctype",
					"name": "Payment Gateway Account",
					"description": _("Setup Gateway accounts.")
				},
				{
					"type": "doctype",
					"name": "POS Profile",
					"label": _("Point-of-Sale Profile"),
					"description": _("Rules to calculate shipping amount for a sale")
				},
				{
					"type": "doctype",
					"name":"Terms and Conditions",
					"label": _("Terms and Conditions Template"),
					"description": _("Template of terms or contract.")
				},
				{
					"type": "doctype",
					"name":"Mode of Payment",
					"description": _("e.g. Bank, Cash, Credit Card")
				},
				{
					"type": "doctype",
					"name":"C-Form",
					"description": _("C-Form records"),
					"country": "India"
				}
			]
		},
		{
			"label": _("Help"),
			"icon": "icon-facetime-video",
			"items": [
				{
					"type": "help",
					"label": _("Chart of Accounts"),
					"youtube_id": "DyR-DST-PyA"
				},
				{
					"type": "help",
					"label": _("Opening Accounting Balance"),
					"youtube_id": "kdgM20Q-q68"
				},
				{
					"type": "help",
					"label": _("Setting up Taxes"),
					"youtube_id": "nQ1zZdPgdaQ"
				}
			]
		}
	]
