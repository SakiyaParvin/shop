# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	# data = get_data(filters)
	return columns, data

def get_columns(filters = None):
	return [
		{
			'fieldname': 'bill_id',
			'label': ('Bill id'),
			'fieldtype': 'Int',
			'width':200
		},
		{
			'fieldname': 'date',
			'label': ('Date'),
			'fieldtype': 'Date',
			'width':200
		},
		{
			'fieldname': 'customer_name',
			'label': ('Customer name'),
			'fieldtype': 'Datetime',
			'options':'Pet Shop Customer',
			'width':200
		},
		{
			"fieldname": "pet_name",
			"label": ("Pet name"),
			"fieldtype": "Data",
			"options": "Pet Shop Pets",
			'width':200
		},
		{
			"fieldname": "pet_category",
			"label": ("Pet category"),
			"fieldtype": "Data",
			"options": "Pet Shop Pets",
			'width':200
		},
		{
			'fieldname': 'phone_number',
			'label': ('Phone number'),
			'fieldtype': 'Int',
			'options':'Pet Shop Customer',
			'width':200
		},
		{
			'fieldname': 'total',
			'label': ('Total'),
			'fieldtype': 'Int',
			'width':200
		},
		{
			'fieldname': 'net_amount',
			'label': ('Net amount'),
			'fieldtype': 'Int',
			'width':200
		}
	]
def get_data(filters):
	data = []
	filter_data = []
	petshoporder = frappe.db.get_list('Pet Shop Customer', {'full_name':filters.get('customer_name') }, 
	[ 'petshoporder', 'bill_id', 'date', 'customer_name', 'phone_number', 'total', 'net_amount' ])
