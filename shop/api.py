from frappe.model.document import Document
import frappe

# @frappe.whitelist()
# def get_select_items_area(item_name1):
# 	area = frappe.db.sql(f""" SELECT i_id,price FROM `tabShop Item` WHERE item_name ='{item_name1}' """, as_dict=True)
# 	return area

@frappe.whitelist()
def get_pets(pets):
	pets = frappe.db.sql(f""" SELECT pet_name,pet_category,pet_price,qty FROM `tabPet Shop Add Pets` WHERE pet_name ='{pets}' """, as_dict=True)
	return pets