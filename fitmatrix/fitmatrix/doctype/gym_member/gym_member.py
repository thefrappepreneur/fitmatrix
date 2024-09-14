# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMember(Document):
	def before_save(self):
		if not self.user_id:
			self.user_id = self.generate_user_id()

	def on_submit(self):
		self.create_user_email()
		self.set_user_permissions()

	def generate_user_id(self):
		"""
		This is function is used to generate gym member email based on id and name
		"""
		# Clean up the name
		cleaned_name = "".join(e for e in self.name1 if e.isalnum())  # remove spaces in member name
		parts = self.name.split("-")
		id = parts[-1]
		# Ensure user_id is formatted to be at least 4 digits, padded with zeros
		user_id_str = f"{id:04}"

		# Combine the name and user_id
		user_email = f"{cleaned_name}-{user_id_str}@gym.local"

		return user_email

	def create_user_email(self):
		if self.user_id:
			doc = frappe.new_doc("User")
			doc.email = self.user_id
			doc.first_name = self.name1
			doc.add_roles("getfitgym user")
			doc.save()
			frappe.db.commit()

	def set_user_permissions(self):
		if self.user_id:
			doc = frappe.new_doc("User Permission")
			doc.user = self.user_id
			doc.allow = "Gym Member"
			doc.for_value = self.name
			doc.save()
			frappe.db.commit()
