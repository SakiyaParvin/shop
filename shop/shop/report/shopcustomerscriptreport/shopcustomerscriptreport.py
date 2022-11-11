# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

from frappe import _
from frappe import _, msgprint
import frappe


def execute(filters=None):
	if not filters:
		filters = {}

	data, columns = [], []

	columns = get_columns()
	lab_test_list = get_lab_tests(filters)

	if not lab_test_list:
		msgprint(_("No records found"))
		return columns, lab_test_list

	data = []
	for lab_test in lab_test_list:
		row = frappe._dict(
			{
				'shop_customer_dob': lab_test.shop_customer_dob,
				'name1': lab_test.name1,
				'shop_customer_age': lab_test.shop_customer_age,
			}
		)
		data.append(row)
	return columns, data, None

def get_columns():
	return [
		{
			"fieldname": "shop_customer_dob",
			"label": ("Shop customer dob"),
			"fieldtype": "Date",
			# "options": "Lab Test",
			"width": "120",
		},
		{
			"fieldname": "name1",
			"label": ("name"),
			"fieldtype": "Data",
			"options": "Shop Customer",
			"width": "120",
		},
		{
			"fieldname": "shop_customer_age",
			"label": ("Shop customer age"),
			"fieldtype": "Int",
			# "options": "Company",
			"width": "120",
		},
	]

def get_lab_tests(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = 'Shop Customer',
		fields = [
			'shop_customer_dob',
			'name1',
			'shop_customer_age',
			# 'shop_customer_address'
			],
		filters = conditions,
		order_by= 'shop_customer_dob desc'
	)
	return data

def get_conditions(filters):
	conditions = {}

	if filters.get("from_date") and filters.get("to_date"):
		conditions["shop_customer_dob"] = ("between", (filters.get("from_date"), filters.get("to_date")))
		# filters.pop("from_date")
	elif filters.get("name1"):
		conditions["name1"] = (filters.get("name1"))
	# elif filters.get("name1"):
	# 	conditions["name1"] = (filters.get("name1"))
	# elif filters.get("shop_customer_age"):
	# 	conditions["shop_customer_age"] = (filters.get("shop_customer_age"))"):
	# 	conditions["shop_customer_age"] = (filters.get("shop_customer_age"))
		# filters.pop("to_date")
		# filters.pop("shop_customer_age")

	for key, value in filters.items():
		if filters.get("key"):
			conditions[key] = value

	return conditions
