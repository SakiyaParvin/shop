// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pet Shop Order Script Report"] = {
	"filters": [
		{
			"fieldname": "bill_id",
			"label": __("Bill id"),
			"fieldtype": "Int",
			"reqd": 1
		},
		{
			"fieldname": "date",
			"label": __("Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.now_date(),
			"reqd": 1
		},
		{
			"fieldname": "customer_name",
			"label": __("Customer name"),
			"fieldtype": "Link",
			// "default": frappe.defaults.get_default("Pet Shop Customer"),
			"options": "Pet Shop Customer"
		},
		{
			"fieldname": "pets",
			"label": __("Pets"),
			"fieldtype": "Link",
			"options": "Pet Shop Add Pets"
		},
		{
			"fieldname": "pet_name",
			"label": __("Pet name"),
			"fieldtype": "Data",
			"options": "Pet Shop Pets"
		},
		{
			"fieldname": "pet_category",
			"label": __("Pet category"),
			"fieldtype": "Data",
			"options": "Pet Shop Pets"
		},
	]
	
};
