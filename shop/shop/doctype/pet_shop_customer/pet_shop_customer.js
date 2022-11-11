// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pet Shop Customer',{

	date_of_birth: function (frm) {
		frappe.call({
		  doc:frm.doc,
		  method:'get_age', 
		  callback:function(r){
			let doc = frm.doc
			doc.age = r.message
			frm.refresh_field('age')
		  }
		})	
	},
	refresh: function(frm) {
		frm.add_custom_button('make order', () => {
            frappe.new_doc('Pet Shop Order', {
                pet_shop_add_pets: frm.doc.name
            })
        })
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Pet Shop', {
                pet_shop_add_pets: frm.doc.name
            })
        })
	},
	
});
