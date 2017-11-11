frappe.ready(function() {
	var me = this;
	var form = $('#page-sign_up_for_erpnext')
	bind_field = new signup(form)
})

signup = Class.extend({
	init:function(form){
		var me = this;
		this.form = form;
		me.get_domain_name()
	},
	get_domain_name:function(){
		var me = this;
		frappe.call({
			method:"mws_erp.multitenancy.web_form.sign_up_for_erpnext.sign_up_for_erpnext.get_domain",
			callback:function(r){
				if (r.message){
					$('input[name=domain]').val(r.message[0].value)
				}
				me.validate_subdomain()
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