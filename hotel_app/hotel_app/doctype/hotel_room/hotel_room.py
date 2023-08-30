# Copyright (c) 2023, MohamedAbdulsalam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HotelRoom(Document):
    # Events: 
    # -----------
    # validate(self): 
	# before_save(self):
	# before_insert(self):
	# after_insert(self):
	# before_submit(self): 
	# on_update(self):
	# on_submit(self):
	# on_cancel(self):
	# on_trash(self):
	# ----------------------------------------

	def validate(self):
		# frappe.msgprint("Helloooo5278272ooooooo")
		doc = frappe.get_doc("Item", self.room_item)
		doc.item_group = "Services"
		doc.db_set("is_stock_item", 0)
		doc.save()
		doc.notify_update()
