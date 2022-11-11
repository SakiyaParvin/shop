# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PetShopAddPets(Document):
	@frappe.whitelist()
	def all_items_session(self,doctype):
		pets = frappe.get_all(doctype,fields=["*"])
		for d in pets:
			self.append("all_items",{
				"pet_name":d.pet_name,
				"pet_category":d.pet_category,
				"pet_price":d.pet_price,
				"qty":d.qty,
				# "price":d.price,
				# "status":d.status,
			})
	def before_submit(self):
		exists = frappe.db.exists(
            "Pet Shop Add Pets",
            {
				"pet_name": self.pet_name,
				# "to_date": (">", self.from_date),
			})
		if exists:
			frappe.throw("pet already exist")
