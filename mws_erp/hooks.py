# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mws_erp"
app_title = "Multitenancy"
app_publisher = "indictrans"
app_description = "DNS based Multitenancy"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "khushal.t@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mws_erp/css/mws_erp.css"
# app_include_js = "/assets/mws_erp/js/mws_erp.js"

# include js, css files in header of web template
web_include_css = "/assets/js/mws-web.min.css"
web_include_js = "/assets/js/mws-web.min.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mws_erp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mws_erp.install.before_install"
# after_install = "mws_erp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mws_erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Site Configurations":{
		"after_insert": "mws_erp.customization.customization.create_site"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"mws_erp.customization.customization.schedule_site"
	]
}
# 	"daily": [
# 		"mws_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"mws_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mws_erp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mws_erp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mws_erp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mws_erp.event.get_events"
# }

