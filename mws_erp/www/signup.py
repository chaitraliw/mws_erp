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


@frappe.whitelist(allow_guest=True)
def set_conf(**kwargs):
	print "_________________",type(kwargs)
	print "++++++++++++555++++++rtrtrt++++++++++++++",frappe.request.url
	sc_doc = frappe.new_doc("Site Configurations")
	sc_doc.subdomain = kwargs.get('subdomain')
	sc_doc.full_name = kwargs.get('full_name')
	sc_doc.email_address = kwargs.get('email_address')
	sc_doc.flags.ignore_mandatory = True
	sc_doc.flags.ignore_permissions = 1
	sc_doc.save()
