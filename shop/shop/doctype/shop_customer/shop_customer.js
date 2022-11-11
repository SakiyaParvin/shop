// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shop Customer', {
	refresh: function(frm) {
		frm.add_custom_button('Make order', () => {
            frappe.new_doc('Shop Customer Order', {
                student: frm.doc.name
            })
        })
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Shop Registration', {
                student: frm.doc.name
            })
        })
	}
});
