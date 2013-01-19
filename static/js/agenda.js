$(document).ready(function() {
	$('#calendar').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek',
		},
		defaultView: 'month',
		editable: true,
		ignoreTimezone: false,

		monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
		monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
		dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
		dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb'],
		allDayText: 'Dia Inteiro',
		buttonText: {
			prev: '&nbsp;&#9668;&nbsp;',
			next: '&nbsp;&#9658;&nbsp;',
			prevYear: '&nbsp;&lt;&lt;&nbsp;',
			nextYear: '&nbsp;&gt;&gt;&nbsp;',
			today: 'hoje',
			month: 'mensal',
			week: 'semanal',
			day: 'diário'
		},

		events: {
	        url: '/events.json',
	        cache: true
	    },
	    dayClick: function(date, allDay, jsEvent, view) {
	        //alert(date + ' has been clicked!');
	    },
	    eventClick: function(calEvent, jsEvent, view) {

	        alert('Event: ' + calEvent.title);
	        // alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
	        // alert('View: ' + view.name);

	        // change the border color just for fun
	        // $(this).css('border-color', 'red');
	        // return false; // <- to not follow the event url
	    },
	    selectable: true,
	    unselectAuto: true,
	    // theme: true,
	});

	$('#botaonovo').click(function(){
		$('.novoevento').slideDown();
		// $('.novoevento').fadeIn();
	});	
	$('#cancel').click(function(){
		$('.novoevento').slideUp();
		// $('.novoevento').fadeOut();
		return false;
	});

});
