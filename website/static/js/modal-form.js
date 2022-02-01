$(document).ready(function() {
	$('button.open_modal_form').click( function(event){
		event.preventDefault();
			$('#modal_form')
				.css('display', 'block')
				.animate({opacity: 1}, 200);
	});
	$('a.open_modal_form').click( function(event){
		event.preventDefault();
		$('#modal_form')
			.css('display', 'block')
			.animate({opacity: 1}, 200);
	});
	$('.open_modal_form_careers').click( function(event){
		event.preventDefault();
		$('#modal_form_careers')
			.css('display', 'block')
			.animate({opacity: 1}, 200);
	});
	$('#modal_close').click( function(){
		$('#modal_form')
			.animate({opacity: 0}, 200,
				function(){
					$(this).css('display', 'none');
				}
			);
	});

	$('#modal_close_careers').click( function(){
		$('#modal_form_careers')
			.animate({opacity: 0}, 200,
				function(){
					$(this).css('display', 'none');
				}
			);
	});
});

$(document).ready(function() {
	$('.open_modal_form_2').click( function(event){
		event.preventDefault();
			$('#modal_form_2')
				.css('display', 'block')
				.animate({opacity: 1, top: '50%'}, 200);
	});
	$('#modal_close_2').click( function(){
		$('#modal_form_2')
			.animate({opacity: 0, top: '45%'}, 200,
				function(){
					$(this).css('display', 'none');
				}
			);
	});
});

$(document).ready(function() {
	$('.open_contacts').click( function(event){
		event.preventDefault();
			$('#contacts')
				.css('display', 'block')
				.animate({opacity: 1, top: '30%'}, 200);
	});
	$('#contacts_close').click( function(){
		$('#contacts')
			.animate({opacity: 0, top: '45%'}, 200,
				function(){
					$(this).css('display', 'none');
				}
			);
	});
});