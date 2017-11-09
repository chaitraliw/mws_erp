# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Multitenancy",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Multitenancy")
		},
		{
			"module_name": "Dashboard",
			"color": "#589494",
			"icon": "fa fa-tachometer",
			"type": "page",
			"link": "dashboard",
			"label": _("Dashboard")
		}
	]
