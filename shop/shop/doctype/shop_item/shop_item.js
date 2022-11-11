// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shop Item', {
	// display_items: function(frm) {
	// 	frm.call({
	// 		method:'all_items_section',
	// 		doc:frm.doc,
	// 		args:{
	// 			doctype:"Shop Item Displays"
	// 		},
	// 		callback:function(r){
	// 			frappe.msgprint(__("successfully updated"))
	// 			frm.refresh_field('item_display')
	// 		}
	// 	})
	// },
	refresh: function(frm) {
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Shop Registration', {
                student: frm.doc.name
            })
        })
	},
	validate: function(frm){
		let row = frm.add_child('Shop Item Displays', {
			"item_name": frm.doc.i_name

		})
	}
});
