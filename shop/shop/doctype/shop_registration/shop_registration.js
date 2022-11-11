// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shop Registration', {
	refresh: function(frm) {
		frm.add_custom_button('Add Item', () => {
            frappe.new_doc('Shop Item', {
                student: frm.doc.name
            })
        })
		frm.add_custom_button('Add Customer', () => {
            frappe.new_doc('Shop Customer', {
                student: frm.doc.name
            })
        })
	}
});
