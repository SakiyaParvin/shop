# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ShopCustomerOrder(Document):
	pass
	# def validate(self):
	# 	self.create_order()
	# def create_order(self): 
	# 	# if self.order_id:
	# 	doc = frappe.get_doc({
	# 		"doctype": "Shop Customer Order Child",
	# 		"customer_name": self.customer_name,
	# 		# "first_item": self.item_1,
	# 		# "first_item_price": self.price_item_1,
	# 		# "second_item": self.item_2,
	# 		# "second_item_price": self.price_item_2,
	# 		# "third_item": self.item_3,
	# 		# "third_item_price": self.price_item_3,
	# 		# "total": self.total_price,
	# 		})
	# 	doc.insert(ignore_permissions=True, ignore_mandatory=True)
	# 	self.order_id = doc.name
