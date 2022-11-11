// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pet Shop Add Pets Script Report"] = {
	"filters": [
		{
			"fieldname": "pet_name",
			"label": __("Pet name"),
			"fieldtype": "Link",
			"options": "Pet Shop Add Pets",
			// "reqd": 1
		},
		{
			"fieldname": "pet_category",
			"label": __("Pet category"),
			"fieldtype": "Data",
			// "reqd": 1
		},
		{
			"fieldname": "pet_price",
			"label": __("Pet price"),
			"fieldtype": "Int",
		},
		{
			"fieldname": "qty",
			"label": __("Qty"),
			"fieldtype": "Int",
		},
		{
			"fieldname": "date",
			"label": __("Date To Start"),
			"fieldtype": "Date",
		},
		{
			"fieldname": "date_of_add",
			"label": __("Date of add"),
			"fieldtype": "Date",
		}
	]
};
