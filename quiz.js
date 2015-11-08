$(document).ready(function() {

		var map = new Map();
	
		$( ".inline" ).each( 
		function(){
		map.put( $(this).id , 0 );
			
			function () {
				$(this).click(fun);
		});
					    

		function fun(event) {

			  
			  	var itsId = $(event.toElement).id;	  
			  
			  if (  !map.value( itsId)  )  {
				 $(event.toElement).fadeTo("fast", 1.0);
				 map.put( itsId, 1);
			 }
			 
			 else 			    {
				 $(event.toElement).fadeTo("fast", 0.3);
				 map.put(itsId, 0);
			 }
			 
		};
		

});



