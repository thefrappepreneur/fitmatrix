# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class FeesCollection(Document):
	def validate(self):
		# This method runs before saving the document
		self.calculate_future_date()

	def calculate_future_date(self):
		# Check if the duration in months is set
		if self.months:
			# Get today's date
			from_date = self.from_date

			# Calculate the future date
			to_date = frappe.utils.add_months(from_date, int(self.months))

			# Set the future date field
			self.to_date = to_date
