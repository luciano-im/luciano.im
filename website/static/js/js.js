$(document).ready(function() {

	//Muestra formulario de contacto
	$('#contact-show').click(function(event) {
		event.preventDefault();
		$('#contact-form').addClass('contact-show');
	});

	//Oculta formulario de contacto
	//mediante el boton cerrar
	$('#contact-form .close').click(function(event) {
		event.preventDefault();
		$('#contact-form').removeClass('contact-show');
	});
	//mediante scroll hacia arriba
	$('#contact-form').on('mousewheel', function(event) {
		if(event.deltaY > 0) {
			$('#contact-form').removeClass('contact-show');
		}
	});

	//Navegacion del elemento NAV
	$('nav li a').click(function(event) {
		event.preventDefault();
		event.stopPropagation();
		var headerHeight = $('header').height();
		var target = $(this).attr('href');
		var topHeight = $(target).offset().top;
		if(headerHeight < 90) {
			$.scrollTo(topHeight-(headerHeight/2), 650, {easing:'swing'});
		} else {
			$.scrollTo(topHeight-(headerHeight), 650, {easing:'swing'});
		}
		// $.scrollTo($(target), 650, {easing:'swing'});
	});

	//Navegacion de botones
	$('#about .more-btn').click(function(event) {
		event.preventDefault();
		event.stopPropagation();
		var headerHeight = $('header').height();
		var target = $(this).attr('href');
		var topHeight = $(target).offset().top;
		if(headerHeight < 90) {
			$.scrollTo(topHeight-(headerHeight/2), 650, {easing:'swing'});
		} else {
			$.scrollTo(topHeight-(headerHeight), 650, {easing:'swing'});
		}
		// $.scrollTo($(target), 650, {easing:'swing'});
	});

	$(window).scroll( function(){
		var browserHeight = $(window).height();
		var navHeight = $('header').height()+10;
		pos = $(window).scrollTop();
		var hola = $('#about').offset().top;
		var hago = $('#services').offset().top;
		var portfolio = $('#portfolio').offset().top;
		var contacto = $('#map-contact').offset().top;

		//nav fixed
		if ($(window).scrollTop() > browserHeight) {
			$('header').addClass('fixed');
		}
		else {
			$('header').removeClass('fixed');
		}

		//home opacity on scroll
		$('#home-content').css({'opacity':( 100-(pos/6) )/100});

		//nav decorator
		if(pos >= browserHeight - navHeight && pos < hago) {
			$('nav li').removeClass('active');
			$('li.hola').addClass('active');
		}

		if(pos >= hago - navHeight && pos < portfolio) {
			$('nav li').removeClass('active');
			$('li.hago').addClass('active');
		}	

		if(pos >= portfolio - navHeight && pos < contacto) {
			$('nav li').removeClass('active');
			$('li.portfolio').addClass('active');
		}		

		if(pos >= contacto - navHeight - 100) {
			$('nav li').removeClass('active');
			$('li.contacto').addClass('active');
		}			

	});

});