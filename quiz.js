$(document).ready(function() {

		var toggler = 0;

/*		var map = new Map();
		map.put( $(this).id , 0 );	
		* 
		* 
		* 
		* 
		//var key = $(event.toElement).id;	  
		//!map.value(key);
		//map.put( itsId, 1);
		//map.put(itsId, 0);
		//To be implemented
*/
//Map to be implemented 	

	
		$( ".inline" ).each( 
			function () {
				$(this).click(fun);
		});
			
		$("#feedback").click(show);

		function fun(event) {
	
			  if (  !toggler  )  {
				 $(event.toElement).fadeTo("fast", 1.0);
				 toggler = 1;
			 }
			 
			 else 			    {
				 $(event.toElement).fadeTo("fast", 0.3);
				 toggler = 0;
			 }
			 
		};
		
		function show(event) {
			alert("You might be at risk! You should see your GP.");
		};
		

});



