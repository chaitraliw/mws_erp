from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	pass
	
@frappe.whitelist(allow_guest=True)
def get_domain():
	return frappe.db.sql("""select value from `tabSingles` where doctype = 'Multitenancy Settings' 
	and field = 'host'""",as_dict=1)
