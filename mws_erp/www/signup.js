window.signup = {
    init: function() {
        this.validate()
    },
    validate: function(){
        var me = this
        $("#button").on("click",function(){
            var name = $("#fname").val().trim()
            var lname = $("#lname").val().trim()
            var comp = $("#company").val().trim()
            var subdomain = $("#subdoman").val().trim()
            var email = $("#email").val().trim()
            if(name.length>100 || !(name.match(/[a-z]/i)) || name.length == ""){
                console.log("++++++=")
                 return false;
              }
        
            frappe.call({
                method: "mws_erp.www.signup.set_conf",
                args: {
                    full_name: name + " " + lname ,
                    company_name: comp,
                    subdomain: subdomain,
                    email_address: email
                },
                callback: function(r) {
                    if(r.message) {
                        console.log(r.message   ,"*****88")
                        window.location.href = location.pathname + "/success"
                        window.location.replace("http://stackoverflow.com")
                        // frappe.render_template(,{"data":"data"})
                    }
                }
            });



        })
    }

}

frappe.ready(function(){
 signup.init()
});



