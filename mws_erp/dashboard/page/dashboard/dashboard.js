frappe.pages['dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Dashboard',
		single_column: true
	});
	
	wrapper.dashboard = new dashboard(wrapper)
}

dashboard = Class.extend({
	init:function(wrapper){
		var me = this;
		this.wrapper_page = wrapper.page;
		this.page = $(wrapper).find('.layout-main-section');
		this.wrapper = $(wrapper).find('.page-content');
		this.get_api_data()
		this.set_interval_for_api_data()
	},
	get_table:function(){
		var me = this;
		html = `<div class='pie-chart'></div>
				</div>`
		me.page.html(html)
		var __html = frappe.render_template("dashboard",{"data":me.data.site_data,"session":me.server_data.has_session})
		$(me.page).find(".pie-chart").empty();
		me.page.find(".pie-chart").append(__html)
	},
	render_graph: function(){
		var me = this;
		
		me.color_codes = {
					1: '#8b1a1a',
            		2: '#FF0000'
        		}
			var chart = c3.generate({
	        bindto:'#space',
	        data: {
				columns:[
						["Total Server Storage Used", me.server_data.used],
						["Storage Available", me.server_data.total_space]
						
				],
				type : 'pie',
				colors: me.color_codes,
        		labels: true
	        },
      	});
	},
	get_data:function(){
		var me =this;
		frappe.call({
			method: "mws_erp.dashboard.page.dashboard.dashboard.get_sites_data",
			callback: function(r) {
				if (r.message){
					me.data = r.message
					me.get_server_data()
				}
			}
		})		
	},
	get_server_data:function(){
		var me =this;
		frappe.call({
			method:"mws_erp.dashboard.page.dashboard.dashboard.get_server_data",
			callback:function(r){
				if(r.message){
					me.server_data = r.message;
					me.get_table();
					me.render_graph();
				}
			}
		})
	},
	get_api_data:function(){
		var me =this;
		frappe.call({
			method:"site_connectivity.customization.connectivity.api_site",
			callback:function(r){
				me.get_data()
			}
		})
	},
	set_interval_for_api_data:function(){
		var me = this;
		setInterval(function () {
			me.get_data()
		}, 10000)
	}
});