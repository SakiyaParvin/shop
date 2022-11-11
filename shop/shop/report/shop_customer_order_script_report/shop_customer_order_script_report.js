// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt
/* eslint-disable */

// frappe.query_reports["Shop Customer Order Script Report"] = {
// 	"filters": [
// 		{
// 			"reqd": 1,
// 			"fieldname":"order_no",
// 			"label": __("Select Order"),
// 			"fieldtype": "Link",
// 			"options": "Shop Customer Order",
			
// 		},
// 		{
// 			"fieldname":"shop_customer_id",
// 			"label": __("Customer id"),
// 			"fieldtype": "Int",
// 			// "options": "Shop Customer",

// 			// "get_query": function() {
// 			// 	return{
// 			// 		"filters":{
// 			// 			"customer_id":customer_id,
// 			// 			// "customer_name":customer_name,
// 			// 		}
// 			// 	}
// 			// }
// 		},
// 	]
// };
frappe.query_reports["Shop Customer Order Script Report"] = {
	"filters": [

		{
			"reqd": 1,
			"fieldname":"order_no",
			"label": __("Select Order"),
			"fieldtype": "Int",
			// "options": "Shop Customer Order",
			
		},
		{
			"fieldname":"customer_id",
			"label": __("Customer id"),
			"fieldtype": "Link",
			"options": "Shop Customer",

		},

		// {
		// 	"fieldname":"price",
		// 	"label": __("Select price"),
		// 	"fieldtype": "Int",
			
		// }
	]
		
};