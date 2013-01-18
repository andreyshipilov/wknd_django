$(function(){
	// Fade title of previous project
	$('#previous-project-title, #next-project-title').animate({'opacity': 0}, 1000);
	
	$('#previous-project a').hover(function(){
		$('#previous-project-title').stop().animate({'opacity': 1});
	}, function(){
		$('#previous-project-title').stop().animate({'opacity': 0});
	});

	// Fade title of next project
	$('#next-project a').hover(function(){
		$('#next-project-title').stop().animate({'opacity': 1});
	}, function(){
		$('#next-project-title').stop().animate({'opacity': 0});
	});

	// Everyone Tweet link
	$('#everyone-tweet-link').delay(1000).animate({'top': -80}).hover(function(){
		$(this).dequeue().animate({'top': -40}, 200);
	}, function(){
	        $(this).dequeue().animate({'top': -80}, 200);
	});
});