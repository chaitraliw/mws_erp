frappe.ready(function() {
	// bind events here
	var me = this;
	var form = $('#page-sign_up_for_erpnext')
	bind_field = new signup(form)
})

signup = Class.extend({
	init:function(form){
		var me = this;
		this.form = form;
		me.get_domain_name()
		me.validate_subdomain()
	},
	get_domain_name:function(){
		var me = this;
		frappe.call({
			method:"frappe.client.get_value",
			args: {
				doctype: "Multitenancy Settings",
				fieldname: "host",
				filters: {"name": "Multitenancy Settings"},

			},
			callback:function(r){
				if (r.message){
					$('input[name=domain]').val(r.message.host)
				}
			}
		})
	},
	validate_subdomain:function(){
		var me = this;
		$('input[name=subdomain]').on("keypress" , function (e) { 
			var keycode = e.charCode || e.keyCode;
  			if (keycode == 46) {
    			return false;
 			 }
  
    })
	}
	
})