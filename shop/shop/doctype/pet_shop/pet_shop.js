// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pet Shop', {
	refresh: function(frm) {
		frm.add_custom_button('Add item', () => {
            frappe.new_doc('Pet Shop Add Pets', {
                pet_shop_add_pets: frm.doc.name
            })
        })
        frm.add_custom_button('Add Customer', () => {
            frappe.new_doc('Pet Shop Customer', {
            	pet_shop_customer: frm.doc.name
            		})
            	})
	},
	
});
