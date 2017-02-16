# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class AuthoritytoLoad(Document):
    def validate(self):
        # Get the sales order under it and check to see if the authority to load flag is set
        if self.has_sales_order():
            res = frappe.get_all('Sales Order', filters={"atl": 1, "name": self.sales_order})
            if res: frappe.throw(frappe._("Authority to load has previously been generated for this sales order"))

    def on_submit(self):
        if self.has_sales_order():
            res = frappe.get_all('Authority to Load', filters=[["sales_order", "=", self.sales_order], ["name", "!=", self.name]])
            if res:
                frappe.throw(frappe._("Authority to load has previously been generated for this sales order"))
            frappe.db.sql(
                "update `tabSales Order` set atl=1 where name='{sales_order}'".format(sales_order=self.sales_order))


    def on_cancel(self):
        if self.has_sales_order():
            frappe.db.sql(
                "update `tabSales Order` set atl=0 where name='{sales_order}'".format(sales_order=self.sales_order))

    def on_trash(self):
        pass

    def on_error(self):
        frappe.errprint("Error occurred while saving...")

    def has_sales_order(self):
        if self.sales_order:
            return True
        return False
