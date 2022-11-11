// Copyright (c) 2022, sakiya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shop Customer Bill', {
    validate: function(frm){
        var temp = cur_frm.doc.items_ordered;
        var sum = 0;
        for ( var i = 0; i < temp.length; i++)
        {
            var obj = temp[i];
            var amount = (obj.price) * (obj.item_qty);
            sum = sum + amount;
        }
        frm.set_value("total",sum)
    },
    before_save:function(frm) {
		frm.set_value('net_amount',frm.doc.total - frm.doc.discount_amount)
    },
    customer_id: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"Shop Customer",
				name:frm.doc.customer_id,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('customer_name',r.message.shop_customer_name)
				}
			})
		})
	},
	refresh: function(frm) {
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Shop Customer Order', {
                student: frm.doc.name
            })
        })
	},
	shop_owner: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"Shop Registration",
				name:frm.doc.shop_owner,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('gst',r.message.gst)
					frm.set_value('contact',r.message.shop_contact)
				}
			})
		})
	},

// frappe.ui.form.on('Shop Item Displays', {
// 	item_name: function(frm) {
// 		frappe.call({
// 			method:"frappe.client.get",
// 			args:{
// 				doctype:"Shop Item Displays",
// 				items_ordered:frm.doc.item_name,
// 			},
// 				callback:(r=>{
// 					if(r.message){
// 						frm.set_value('price',r.message.price)
// 					}
// 				})
// 		})
// 	},
});
