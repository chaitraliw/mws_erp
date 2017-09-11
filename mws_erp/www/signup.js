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
            
            console.log("***####################",name,lname,comp,subdomain,email)
            if(name.length>100 || !(name.match(/[a-z]/i)) || name.length == ""){
                console.log("++++++=")
                 return false;
              }
        
            frappe.call({
                method: "mws_erp.customization.customization.set_conf",
                args: {
                    "full_name": name+" "+lname ,
                    "company_name": comp,
                    "subdomain": subdomain,
                    "email_address": email
                },
                callback: function(r) {
                    if(r.message) {
                    }
                }
            });



        })
    }

}

frappe.ready(function(){
 signup.init()
});



