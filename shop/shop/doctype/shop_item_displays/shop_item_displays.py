# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ShopItemDisplays(Document):
	pass
	# def validate(self):
	# 	self.create_display()
	# def create_display(self):
	# 	if self.status == 'Available' and not self.item_id: 
	# 		doc = frappe.get_doc({
	# 			"doctype": "Shop Item",
	# 			"i_name": self.item_name,
	# 			"i_image": self.item_image,
	# 			"i_vehicle": self.vehicle,
	# 			"i_price": self.price,
	# 			"i_status": self.status,
	# 			})
	# 		doc.insert(ignore_permissions=True, ignore_mandatory=True)
	# 		self.item_id = doc.name
