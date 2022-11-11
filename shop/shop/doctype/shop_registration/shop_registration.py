# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class ShopRegistration(WebsiteGenerator):
	pass
	# def validate(self):
	# 	self.create_shop()
	# def create_shop(self):
	# 	if self.shop_id:
	# 		doc = frappe.get_doc({
	# 			"doctype": "Shop Registration",
	# 			"shop_name": self.shop_name,
	# 			"shop_image": self.shop_image,
	# 			"shop_address": self.shop_address,
	# 			"shop_contact": self.shop_contact,
	# 			})
	# 		doc.insert(ignore_permissions=True, ignore_mandatory=True)
	# 		self.shop_id = doc.name
