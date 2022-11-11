// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shop Customer Order', {
	
	refresh: function(frm) {
		frm.add_custom_button('Bill', () => {
            frappe.new_doc('Shop Customer Bill', {
                student: frm.doc.name
            })
        })
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Shop Customer', {
                student: frm.doc.name
            })
        })
	},
	
	customer_name: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"Shop Customer",
				name:frm.doc.customer_name,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('customer_id',r.message.shop_customer_id)
				}
			})
		})
	},
	
	
});


	


	
