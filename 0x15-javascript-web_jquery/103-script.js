$(document).ready(function() {
        	function translate() {
            	const langCode = $('#language_code').val();
                
                if (langCode) {
                	$.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function(data) {
                    	$('#hello').text(data.hello);
                    });
                }
            }
            
          $('#btn_translate').click(translate);
          $('#language_code').keydown(function(event) 				{
          		if (event.which === 13) {
                	translate()
                }
          	});
        });
