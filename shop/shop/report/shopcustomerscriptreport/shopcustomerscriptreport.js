// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["ShopCustomerScriptReport"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			// "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			// "default": frappe.datetime.now_date(),
			"reqd": 1
		},
		{
			"fieldname": "name1",
			"label": __("name"),
			"fieldtype": "Link",
			"default": frappe.defaults.get_default("name1"),
			"options": "Shop Customer",
			"reqd": 1

		},
		{
			"fieldname": "shop_customer_dob",
			"label": __("Shop customer dob"),
			"fieldtype": "Date",
			// "default": frappe.datetime.now_date(),
			"reqd": 1
		},
				
		{
			"fieldname": "shop_customer_age",
			"label": __("Shop customer age"),
			"fieldtype": "Int",
			"default": frappe.defaults.get_default("Shop customer age"),
			// "options": "Lab Test Template"
		},
	]
};

