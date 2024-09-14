// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Fees Collection", {
	onload: function (frm) {
		// Code to run when the document form is loaded
		console.log("Document loaded:", frm.doc);
		if (!frm.doc.from_date) {
			frm.set_value("from_date", frappe.datetime.get_today());
		}
	},
	months: (frm) => set_to_date(frm),
	from_date: (frm) => set_to_date(frm),
});
let set_to_date = function (frm) {
	// Trigger calculation when the duration field is changed
	let months_str = frm.doc.months;

	// Extract number of months from the selected duration string
	let months = parseInt(months_str, 10);

	if (!isNaN(months)) {
		// Get today's date
		let from_date = frm.doc.from_date;

		// Calculate the future date
		let future_date = frappe.datetime.add_months(from_date, months);

		// Set the future date field
		frm.set_value("to_date", future_date);
	}
};
