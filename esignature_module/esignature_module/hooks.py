app_name = "esignature_module"
app_title = "Esignature Module"
app_publisher = "dexciss"
app_description = "frontend app"
app_email = "smunde@dexciss.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/esignature_module/css/esignature_module.css"
# app_include_js = "/assets/esignature_module/js/esignature_module.js"

# include js, css files in header of web template
# web_include_css = "/assets/esignature_module/css/esignature_module.css"
# web_include_js = "/assets/esignature_module/js/esignature_module.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "esignature_module/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "esignature_module/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "esignature_module.utils.jinja_methods",
#	"filters": "esignature_module.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "esignature_module.install.before_install"
# after_install = "esignature_module.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "esignature_module.uninstall.before_uninstall"
# after_uninstall = "esignature_module.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "esignature_module.utils.before_app_install"
# after_app_install = "esignature_module.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "esignature_module.utils.before_app_uninstall"
# after_app_uninstall = "esignature_module.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "esignature_module.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"esignature_module.tasks.all"
#	],
#	"daily": [
#		"esignature_module.tasks.daily"
#	],
#	"hourly": [
#		"esignature_module.tasks.hourly"
#	],
#	"weekly": [
#		"esignature_module.tasks.weekly"
#	],
#	"monthly": [
#		"esignature_module.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "esignature_module.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "esignature_module.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "esignature_module.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["esignature_module.utils.before_request"]
# after_request = ["esignature_module.utils.after_request"]

# Job Events
# ----------
# before_job = ["esignature_module.utils.before_job"]
# after_job = ["esignature_module.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"esignature_module.auth.validate"
# ]

website_route_rules = [{'from_route': '/esignature_ui/<path:app_path>', 'to_route': 'esignature_ui'},]