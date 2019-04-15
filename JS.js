// JavaScript File
function main() {
  
  $('.projects').hide();
  
  $('.projects-button').on('click', function() {
		$(this).next().slideToggle(400);
    $(this).toggleClass('active');
    $(this).text('Now, try out our calculators!');
	});
}

$(document).ready(main);