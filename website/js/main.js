$(document).ready(function(){
  $('#butt').click(function(){	
	$.ajax({
	  url: "http://localhost:5000/",
	  context: document.body
	}).done(function( data ) {
		$("#test").text(data);
	}); 
  });
});
