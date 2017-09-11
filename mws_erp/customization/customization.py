# -*- coding: utf-8 -*-
# Copyright (c) 2015, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _,msgprint
from frappe.model.document import Document
import json
import subprocess
import os
import hashlib


# def create_site(doc, method):
# 	print "$$$$$$$$$$$$$$$$$$$$$$$trtrtrtrt$$$$$$$$$$"
# 	"""Check site exist/create"""
# 	if ' ' in doc.name:
# 		print "********************8"
# 		frappe.throw(_('Please Remove space in host name'))
# 	else: 
# 		print "_____dfsfsf_____dfdfdfdfgfdgfdg______"
# 		setup_site(doc)


# def setup_site(doc):
# 	"""install-app on site creation/drop-site """	
# 	print "*************************"
# 	settings = frappe.get_doc('Multitenancy Settings')
# 	mysql_pwd = settings.get_password('mysql_password')
# 	root_pwd = settings.get_password('root_password')
# 	admin_pwd = "admin"
# 	site_name =  doc.subdomain

# 	if mysql_pwd and root_pwd:
# 		try:
# 			cmds = [                                           
# 				{
# 					"../bin/bench new-site --mariadb-root-password {0} --admin-password {1} {2}".format(
# 					root_pwd, admin_pwd, site_name): "Creating New Site ..........: {0}".format(site_name)
# 				},
# 				{
# 					"../bin/bench --site {0} enable-scheduler".format(site_name):"***Enabling Scheduler*****"
# 				},
# 				{ 
# 					"../bin/bench --site {0} install-app erpnext".format(site_name): "Installing ERPNext App..."
# 				},
# 				{
# 					"../bin/bench --site {0} migrate".format(site_name): "******Migrating Bench***********"
# 				},
# 				{
# 					"../bin/bench setup nginx --yes".format('YES'):"***Production setup***"
# 				},
# 			]

# 			for cmd in cmds:
# 				exec_cmd(cmd, cwd='../', domain_name=site_name)
# 			p = os.system('echo %s|sudo -S %s' % (root_pwd, 'service nginx reload'))
# 			# cust_doc = frappe.get_doc("Customer",cust)
# 			# cust_doc.is_site = 1
# 			# cust_doc.site_name = site_name
# 			# cust_doc.save()
# 			# frappe.reload_doc("selling", "doctype", "customer")
# 			frappe.msgprint(_("Site created for domain <b>{0}</b>".format(site_name)))
# 			send_mail(doc)

# 		except Exception, e:
# 			print "Into TRACEBACK_______________________________",frappe.get_traceback()
# 			# error_doc = frappe.new_doc("Error Log")
# 			# error_doc.error = frappe.get_traceback()
# 			# error_doc.save()
# 			cmd = "echo Removing Sites......... && ../bin/bench drop-site --root-password {0} {1}".format(root_pwd,site_name)
# 			p = subprocess.Popen(cmd, cwd='../', shell=True, stdout=None, stderr=None)


# def exec_cmd(cmd_dict, cwd='../', domain_name=None):
# 	"""Executing shell installing-app"""
	
# 	key = cmd_dict.keys()[0]
# 	val = cmd_dict[key]
# 	cmd = "echo {desc} && {cmd}".format(desc=val, cmd=key) if val else key
# 	p = subprocess.Popen(cmd, cwd=cwd, shell=True, stdout=None, stderr=None)
# 	return_code = p.wait()
# 	if return_code > 0:
# 		frappe.throw(_("Error while executing command : %s \n for site  : %s \n in directory %s"%(cmd, domain_name,os.getcwd())))


# def send_mail(doc):
# 	"""Notify vendor for Subscription details"""
#  	print "**************************SEND MAIL"
#  	try:
# 		frappe.sendmail(recipients= doc.email_address, subject="Subscription Details",
# 			message=render_mail_template(doc), delayed=False)
# 	except frappe.OutgoingEmailError:
# 		pass 


# def render_mail_template(doc):
# 	"""template for subscription detals """
	
# 	return frappe.render_template("mws_erp/templates/erp.html",
# 		{
# 			"data":{
# 				"site": doc.subdomain,

# 			}
# 		}
# 	)

@frappe.whitelist(allow_guest=True)
def set_conf(**kwargs):
	print "++++++++++++555++++++++++++++++++++",kwargs
	# sc _doc = frappe.new_doc("Site Configurations")
	# sc_doc.subdomain = "kwargs.get('subdomain')"
	# sc_doc.full_name = kwargs.get('full_name')
	# sc_doc.email_address = kwargs.get('email_address')
	# sc_doc.flags.ignore_mandatory = True
	# sc_doc.flags.ignore_permissions = 1
	# sc_doc.insert()
	# print "__________________________"