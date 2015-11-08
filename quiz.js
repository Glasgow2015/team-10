$(document).ready(function() {

		var array = new Array();
		
		var i = 0;
		for (i; i<10; i++) {
			array[i] = 0; 
		}	

		//console.log(id + " ");
		
		
		$( ".inline" ).each( function () {

		$(this).click( function() {
			var idNo = (this).id;
				    

			 if (!array[idNo])  {
				 $(this).fadeTo("fast", 1.0);
				 array[idNo] = 1;
			 }
			 
			 else 			    {
				 $(this).fadeTo("fast", 0.3);
				 array[idNo] = 0;
			 }
			 
			 
			
		});
		
		});
					    
			    

		
		

});
