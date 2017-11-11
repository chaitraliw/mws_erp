from __future__ import unicode_literals
import frappe
import MySQLdb
from MySQLdb.times import DateTimeDeltaType
from subprocess import Popen, PIPE, STDOUT
import subprocess
import os 
from frappe.installer import get_root_connection
from frappe import _,msgprint
from frappe.model.db_schema import DbManager
from frappe.utils import flt, cstr, cint
from collections import defaultdict



@frappe.whitelist()
def get_sites_data():
	data = frappe.get_all("Site Configurations")
	all_data = defaultdict(list)
	try:
		for row in data:
			conf_doc = frappe.get_doc("Site Configurations",row.get('name'))
			settings_doc = frappe.get_doc("Multitenancy Settings")
			if conf_doc.is_site == 1:
				all_data[row.get('name')].append({"company_name":conf_doc.company_name,"full_name":conf_doc.full_name,
								 "email_address":conf_doc.email_address	,"creation":conf_doc.creation,
								 "last_login":conf_doc.last_signup,"customer_count":conf_doc.customer_count,
								 "is_site":conf_doc.is_site,"domain":(conf_doc.name.lower() + settings_doc.host)})
	except Exception, e:
		frappe.msgprint(_("Please Wait.. Refresh after some time.."))
		error_log = frappe.new_doc("Error Log")
		error_log.method = "Onload Dashboard"
		error_log.error = e
		error_log.save()

	return {"site_data":all_data}


@frappe.whitelist()
def get_server_data():
	process = subprocess.Popen("du -hs sites", cwd='../', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	process_comm = process.communicate()
	used = flt(process_comm[0].split()[0].split('M')[0])
	total_space = total_site_space()
	settings_doc = frappe.get_doc("Multitenancy Settings")
	return {"used" : round((used/1024),4),"total_space":total_space,"has_session":settings_doc.session_count}

def total_site_space():
	sites = frappe.utils.get_sites()
	space_list = []
	if os.path.exists('currentsite.txt'):
		with open('currentsite.txt') as f:
			currentsite = [f.read().strip()]
	for site in sites:
		if site not in currentsite:
			site_config = frappe.get_site_config(site_path=site)
			doc = frappe.get_doc("Site Configurations",site.split(".")[0])
			if doc.is_allotted == 0:
				process = subprocess.Popen("bench --site {0} set-limit space 1".format(site), cwd='../', shell=True, stdout=None, stderr=None)
				doc.is_allotted = 1
				doc.save()
			space = site_config.get('limits').get('space')
			space_list.append(space)
	return sum(space_list)


