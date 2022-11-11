# Copyright (c) 2022, sakiya and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
from six import iteritems
from frappe import _
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	if not data:
		frappe.msgprint(_("no records found")) 
		return columns, data
	datas = []
	for d in data:
		row = frappe._dict({
			'pet_name': d.pet_name,
			'pet_category': d.pet_category,
			'pet_price': d.pet_price,
			'qty': d.qty,
			'date_of_add': d.date_of_add,
			'date': d.date,

		
		})
		datas.append(row)
	chart = get_chart_data(datas)
	report_summary = get_report_summary(datas)
	return columns, datas, None, chart, report_summary

def get_columns():
	return [
		{
			"fieldname": "pet_name",
			"label": ("Pet name"),
			"fieldtype": "Data",
			# "options": "Pet Shop Pets",
			'width':200
		},
		{
			"fieldname": "pet_category",
			"label": ("Pet category"),
			"fieldtype": "Data",
			# "options": "Pet Shop Pets",
			'width':200
		},
		{
			'fieldname': 'pet_price',
			'label': ('Pet price'),
			'fieldtype': 'Int',
			# "options": "Pet Shop Pets",
			'width':200
		},
		{
			'fieldname': 'qty',
			'label': ('Qty'),
			'fieldtype': 'Int',
			# "options": "Pet Shop Pets",
			'width':200
		},
		{
			'fieldname': 'date_of_add',
			'label': ('Date of add'),
			'fieldtype': 'Datetime',
			# "options": "Pet Shop Pets",
			'width':200
		},
		{
			'fieldname': 'date',
			'label': ('Date of Start'),
			'fieldtype': 'Data',
			# "options": "Pet Shop Pets",
			'width':200
		}
	]

def get_data(filters):
	datas = frappe.get_all(
		doctype = 'Pet Shop Add Pets',
		fields = ['pet_name','pet_category','pet_price','qty','date_of_add','date'],
		order_by = 'pet_name desc'
		)
	data = []
	filter_data = []
	if filters.get('pet_name'):
		for i in datas:
			if i.get('pet_name') == filters.get('pet_name'):
				filter_data.append(i)
			datas = filter_data
	filter_data = []
	if filters.get('pet_category'):
		for i in datas:
			if i.get('pet_category') == filters.get('pet_category'):
				filter_data.append(i)
			datas = filter_data
	filter_data = []
	if filters.get('pet_price'):
		for i in datas:
			if i.get('pet_price') == filters.get('pet_price'):
				filter_data.append(i)
			datas = filter_data
	filter_data = []
	if filters.get('qty'):
		for i in datas:
			if i.get('qty') == filters.get('qty'):
				filter_data.append(i)
			datas = filter_data
	filter_data = []
	if filters.get('date_of_add'):
		for i in datas:
			if i.get('date_of_add') == filters.get('date_of_add'):
				filter_data.append(i)
			datas = filter_data
	filter_data = []

	# conditions = {
	# 	'docstatus': ('=', 1)
	# }
	# if filters.get('date'):
	# 	return  conditions

		
	return datas
	# data = []
	# filter_data = []
	# employee = frappe.db.get_all('Pet Shop Pets',['pet_name', 'pet_category', 'pet_price', 'qty'])
	# for i in employee:
	# 	attendance = {'pet_name':i.pet_name, 'pet_category':i.pet_category, 'pet_price':i.pet_price, 'qty':i.qty}
	# 	data.append(attendance)

		# if filters.get('pet_price'):
		# 	for i in data:
		# 		if i.get('pet_price') == filters.get('pet_price'):
		# 			filter_data.append(i)
		# 			data = filter_data
		# filter_data = []
	
def get_chart_data(datas):
	if not datas:
		return None	

	labels = ['Pet price > 5000','Pet price < 5000']
	pet_price_data = {
		'Pet price > 5000' : 0,
		'Pet price < 5000' : 0,
	}
	datasets = []
	for entry in datas:
		if entry.pet_price > 5000:
			pet_price_data['Pet price > 5000'] += 1
		else:
			pet_price_data['Pet price < 5000'] += 1
	datasets.append({
		'name': 'Pet price',
		'values': [pet_price_data.get('Pet price > 5000'),pet_price_data.get('Pet price < 5000')]
	})
	chart = {
		'data': {
			'labels': labels,
			'datasets': datasets
		},
		'type':'pie',
		'height': 300,
	}

	return chart

def get_report_summary(datas):
	if not datas:
		return None	
	pet_price_below_5000, pet_price_above_5000 = 0, 0

	for entry in datas:
		if (entry.pet_price > 5000):
			pet_price_above_5000 += 1
		else:
			pet_price_below_5000 += 1
	return [{
		'value': pet_price_below_5000,
		'indicator': 'Green',
		'label': 'Pet price below 5000',
		'datatype': 'Int'
	},
	{
		'value': pet_price_above_5000,
		'indicator': 'Blue',
		'label': 'Pet price above 5000',
		'datatype': 'Int'
	}		
	]
		
