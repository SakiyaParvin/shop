# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dateutil import relativedelta
from datetime import datetime

class PetShopCustomer(Document):
	def validate(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
		self.get_list()
		self.mobile_number_validation()
	
	@frappe.whitelist()
	def get_age(self):
		if(self.date_of_birth):
			today = datetime.now()
			date_of_birth = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
			t = relativedelta.relativedelta(today, date_of_birth)
			return t.years

	def get_list(self):
		doc = frappe.get_list('Pet Shop Customer',
				filters={},
				fields=['full_name']
		)
		for d in doc:
			frappe.msgprint(("{0} is a member of pet care").format(d.full_name))
	
	def mobile_number_validation(self):
		if self.phone_number:
			if not (self.phone_number).isdigit():
				frappe.msgprint("Contact Number Accept Digits Only")
			if len(self.phone_number)>10:
				frappe.msgprint("Contact Number must be 10 Digits")
			if len(self.phone_number)<10:
				frappe.msgprint("Contact Number must be 10 Digits")
	


