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
                                        var {{ param.name }} = $('input#{{ method.slug }}_{{ param.name }}').val();
                                        if ({{ param.name }} == '')
                                        {
                                            {{ param.name }} = {{ param.default_value }};
                                        }
                                        {% if param.get_or_url == 'get' %}
                                        param_url = param_url + "{{ param.name }}=" + {{ param.name }} + "&";
                                        {% else %}
                                        api_url = api_url + "/" + {{ param.name }};
                                        {% endif %}
                                    {% endif %}
                                    {% endfor %}
                                    
                                {% endif %}
                                var call_url = api_url + param_url;
                                $(this).parent().children('pre').replaceWith('<pre>' + call_url + '</pre>');
                                
                               $.ajax({
                                  url: call_url,
                                  dataType: 'jsonp',
                                  success: function(data){
                                    $('<h6>Response</h6><pre>' + JSON.stringify(data) + '</pre>').appendTo('#{{ method.slug }}_response')
                                  }
                               });
                               
                            });
                            {% endfor %}
                        {% endfor %}
                    {% endfor %}
		  });