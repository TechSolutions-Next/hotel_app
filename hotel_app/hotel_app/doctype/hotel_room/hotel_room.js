// Copyright (c) 2023, MohamedAbdulsalam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Hotel Room', {
	after_save: function(frm) {
		if (frm.doc.has_amenities) {
			let row = frm.add_child('room_amenity', {
				item: 'شاشة تلفزيون مسطح',
				billable: 0
			});
			// frm.refresh_field('room_amenity');
		}
	},
	validate:function(frm){
		frm.set_value('room_name',frm.doc.room_item +"-"+ frm.doc.room_no)
	},
	refresh:function(frm){
		frm.add_custom_button('Open Hotel Room Type', () => {
			frappe.set_route('Form', 'Hotel Room Type', frm.doc.hotel_room_type);
		});
	}
	});

