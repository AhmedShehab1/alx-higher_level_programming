$(document).ready(function() {
		        	$('#btn_translate').click(function() {
     		if ($('#language_code').val()) {
            	$.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`, function(data, status) {
                	$('#hello').text(data.hello);
                });
            }
     });
});
