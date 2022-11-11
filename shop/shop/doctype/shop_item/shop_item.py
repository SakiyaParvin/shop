# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ShopItem(Document):
	@frappe.whitelist()
	def all_items_section(self,doctype):
		data=frappe.get_all(doctype,fields=["*"])
		for d in data:
			self.append("item_display",{
				"item_id":d.item_id,
				"item_name":d.item_name,
				"item_image":d.item_image,
				"vehicle":d.vehicle,
				"price":d.price,
				"status":d.status,
			})
