
$(document).ready(function() {
   $('.action').hide();
   
   $('.api_heading').click(function(){
       $(this).parent().children('.action').slideToggle('slow');	  
   });
   $('.clear').click(function(){
       $(this).parent().children('.response').empty();	  
   });
   {% for api in apis %}
       {% for apiobj in api.apiobject_set.all %}
	   {% for method in apiobj.apimethod_set.all %}
	   $('#call_{{ method.slug }}').click(function(){
	       {% if method.parameter.all %}
		   var param_url = "?";
		   var api_url = "{{ method.api_url }}";
		   {% for param in method.parameter.all %}
		   {% if param.type == 'text' %}
		       var var_{{ param.name }} = $('input#{{ method.slug }}_{{ param.name }}').val();
		       if (var_{{ param.name }} == '')
		       {
			   var_{{ param.name }} = "{{ param.default_value }}";
		       }
		       {% if param.get_or_url == 'get' %}
		       param_url = param_url + "{{ param.name }}=" + var_{{ param.name }} + "";
		       {% endif %}
		       {% if param.get_or_url == 'url' or param.get_or_url == 'delete' %}
		       api_url = api_url + "/" + var_{{ param.name }};
		       
		       {% endif %}
		   {% endif %}
		   {% endfor %}
		   
	       {% endif %}
	       var call_url = api_url + param_url + "&format=json";
	       $(this).parent().children('pre').replaceWith("<pre>{{ method.get_type_display }}: <a href='" + call_url + "'>" + call_url + "</a></pre>");
	       
	       {% if method.type == 'post' or method.type == 'put' %}
	       var dataString = "";
		 {% for param in method.parameter.all %}
		   {% if param.type != 'no_input' %}
		     dataString = dataString + "&{{ param.name }}=" + var_{{ param.name }};
		   {% endif %}
		 {% endfor %}
	       {% endif %}
	       
	      $.ajax({
		 url: call_url,
		 dataType: 'jsonp',
		 type: "{{ method.get_type_display }}",
		 {% if method.type == 'post' or method.type == 'put' %}
		 data: dataString,
		 
		 {% endif %}
		 processData: false,
		 contentType: "application/x-www-form-urlencoded",
		 success: function(data){
		 
		   $('<h6>Response</h6><pre>' + JSON.stringify(data) + '</pre>').appendTo('#{{ method.slug }}_response')
		 }
	      });
	      
	      
	   });
	   {% endfor %}
       {% endfor %}
   {% endfor %}
 });
