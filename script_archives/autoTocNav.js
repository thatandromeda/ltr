// Written by Jeremy Darrington, Princeton University Library, http://libguides.princeton.edu/politics
// Let me know if you have suggestions for improvements, bug fixes, etc.
// This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, http://creativecommons.org/licenses/by-nc-sa/4.0/

//you need to first put all your boxes in the center column and create an empty box in the left column for the TOC
$(document).ready(function() {
	var $boxID = [];
	var $boxTitle = [];
//get box titles
	$('div[id^="wrapbox"] .headerbox h2').each(function() {
		var hText = $(this).text();
		var patt1 = /\d\)\;/;
		if (hText.match(patt1)) {
		$boxTitle.push(hText.slice(hText.search(patt1)+3));
		} else {
		$boxTitle.push(hText);
		}
	});
//get box IDs
	$('div[id^="wrapbox"]').each(function() {
		$boxID.push($(this).attr("id"));
	});
//populate the nav box with box titles
	var $tocBox = $('div[id='+$boxID[0]+'] div[id^="content"]');
	for (i=1; i<$boxTitle.length; i++) {
		$tocBox.append('<div class="boxNav" name='+$boxID[i]+'><a> '+$boxTitle[i]+'</a></div>');
		}
//hide all but the first content box on load
	
//if url is for an indiv box, select that one and hide other content boxes; if not, show only first content box and make the first TOC entry the currently selected item
	if (location.hash) {
			var $boxNum = location.hash.slice(+1);
			 // $('div[id='+$boxNum+']').show();
			 // $tocBox.append('<div>'+$boxNum+'</div>');
			for (i=1; i<$boxID.length; i++) {
				if ($boxID[i]==('wrapbox'+$boxNum)) { 
					$('div[id='+$boxID[i]+']').show();
					window.scrollTo(0,0);
					$('div[name="wrapbox'+$boxNum+'"]').addClass('currentNav').prepend('<i class="icon-double-angle-right icon-large"></i>');
				}
				else {
					$('div[id='+$boxID[i]+']').hide();
				}
			}
		}
	else {
		for (i=2; i<$boxID.length; i++) {
			$('div[id='+$boxID[i]+']').hide();
		}
		$('.boxNav').filter(':first').addClass('currentNav').prepend('<i class="icon-double-angle-right icon-large"></i>');
		}
//show the selected box when clicked
	$('.boxNav').click(function() {
    	var selectedNav = $('.currentNav');
	    $(selectedNav).toggleClass('currentNav');
	    $(this).prepend($('.icon-double-angle-right'));
	    $(this).toggleClass('currentNav');
	    for (i=1; i<$boxTitle.length; i++) {
			if ($(this).attr('name')==$boxID[i] ) {
				$('div[id='+$boxID[i]+']').show();
				window.location.hash = $('div[id='+$boxID[i]+']').children("div").attr("id");
				window.scrollTo(0,0);
			} else {
				$('div[id='+$boxID[i]+']').hide();
			}
		}
	});

});