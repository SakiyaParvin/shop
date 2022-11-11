// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pet Shop Add Pets', {
	refresh: function(frm) {
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Pet Shop', {
                pet_shop: frm.doc.name
            })
        })
	},
	// pets: function(frm){
	// 	let row = frm.add_child('Pet Shop Pets', {
	// 		"pet_name": frm.doc.pet_name,
    //         "pet_category":frm.doc.pet_category,
	// 		"pet_price":frm.doc.pet_price,
	// 		"qty":frm.doc.qty,
	// 	})
	// },
    pets: function(frm) {
        	frm.call({
        		method:'all_items_session',
        		doc:frm.doc,
        		args:{
        			doctype:"Pet Shop Pets"
        		},
        		callback:function(r){
        			frappe.msgprint(__("success"))
        			frm.refresh_field('all_items')
        		}
        	})
        },
});
