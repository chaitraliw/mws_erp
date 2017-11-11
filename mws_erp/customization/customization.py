# -*- coding: utf-8 -*-
# Copyright (c) 2015, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _,msgprint
from frappe.model.document import Document
import json
import subprocess
from subprocess import Popen,PIPE
import os
import hashlib
import re
import requests
import json


def create_site(doc, method):
	"""Check site exist/create"""
	
	if ' ' in doc.name:
		frappe.throw(_('Please Remove space in host name'))
	
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', doc.email_address)
	if match == None:
		frappe.throw(_('Email not valid'))



def setup_site(i):
	"""install-app on site creation/drop-site """	
	
	doc = frappe.get_doc("Site Configurations",i.get('name'))
	doc.queued = 1
	doc.save()
	print "******************",doc.__dict__
	settings = frappe.get_doc('Multitenancy Settings')
	mysql_pwd = settings.get_password('mysql_password')
	root_pwd = settings.get_password('root_password')
	admin_pwd = "admin"
	site_name =  i.get('name').lower()+settings.get('host')

	if mysql_pwd and root_pwd:
		try:
			cmds = [                                           
				{
					"../bin/bench new-site --mariadb-root-password {0} --admin-password {1} {2}".format(
					mysql_pwd, admin_pwd, site_name): "Creating New Site ..........: {0}".format(site_name)
				},
				{
					"../bin/bench --site {0} enable-scheduler".format(site_name):"***Enabling Scheduler*****"
				},
				{ 
					"../bin/bench --site {0} install-app erpnext".format(site_name): "Installing ERPNext App..."
				},
				{ 
					"../bin/bench --site {0} install-app site_connectivity".format(site_name): "Installing Site Connectivity App..."
				},
				{
					"../bin/bench --site {0} migrate".format(site_name): "******Migrating Bench***********"
				},
				{
					"../bin/bench setup nginx --yes".format('YES'):"***Production setup***"
				},
			]

			for cmd in cmds:
				exec_cmd(cmd, cwd='../', domain_name=site_name)
			p = os.system('echo %s|sudo -S %s' % (root_pwd, 'service nginx reload'))
			frappe.msgprint(_("Site created for domain <b>{0}</b>".format(site_name)))

		except Exception, e:
			cmd = "echo Removing Sites......... && ../bin/bench drop-site --root-password {0} {1}".format(root_pwd,site_name)
			p = subprocess.Popen(cmd, cwd='../', shell=True, stdout=None, stderr=None)
			error_log = frappe.new_doc("Error Log")
			error_log.method = "setup_site"
			error_log.error = e
			error_log.save()


def exec_cmd(cmd_dict, cwd='../', domain_name=None):
	"""Executing shell installing-app"""
	
	key = cmd_dict.keys()[0]
	val = cmd_dict[key]
	cmd = "echo {desc} && {cmd}".format(desc=val, cmd=key) if val else key
	p = subprocess.Popen(cmd, cwd=cwd, shell=True, stdout=None, stderr=None)
	return_code = p.wait()
	if return_code > 0:
		frappe.throw(_("Error while executing command : %s \n for site  : %s \n in directory %s"%(cmd, domain_name,os.getcwd())))


def send_mail(doc, settiing_doc):
	"""Notify vendor for Subscription details"""
 	try:
		frappe.sendmail(recipients= doc.email_address, subject="Subscription Details",
			message=render_mail_template(doc, settiing_doc), delayed=False)
	except frappe.OutgoingEmailError:
		pass 


def render_mail_template(doc, settiing_doc):
	"""template for subscription detals """
	
	return frappe.render_template("mws_erp/templates/erp.html",
		{
			"data":{
				"site": doc.subdomain.lower()+settiing_doc.get('host'),
				"user_name": doc.full_name

			}
		}
	)


def schedule_site():
	"""schedule sites for the req data"""
	
	dict_ = frappe.db.sql("""select name,full_name,email_address,company_name,is_site
		                    from `tabSite Configurations` where queued = '0' """,as_dict=1)
	for i in dict_:
		setup_site(i)
		doc = frappe.get_doc("Site Configurations",i.get('name'))
		doc.is_site = 1
		doc.save()
		send_mail(doc,frappe.get_doc("Multitenancy Settings"))