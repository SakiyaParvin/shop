// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pet Shop Order', {
	validate: function(frm){
        var temp = cur_frm.doc.items;
        var sum = 0;
        for ( var i = 0; i < temp.length; i++)
        {
            var obj = temp[i];
            var amount = (obj.pet_price) * (obj.qty);
            sum = sum + amount;
        }
        frm.set_value("total",sum)
    },
    before_save:function(frm) {
		frm.set_value('net_amount',frm.doc.total - frm.doc.discount)
    },
	customer_name: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"Pet Shop Customer",
				name:frm.doc.customer_name,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('customer_name',r.message.full_name)
					frm.set_value('phone_number',r.message.phone_number)
				}
			})
		})
	},
	refresh: function(frm) {
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Pet Shop Customer', {
                student: frm.doc.name
            })
        })
	},
});
