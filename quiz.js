$(document).ready(function() {

	//function() { console.log("LALLALA"); };
	
    //document.getElementById(boxNo).innerHTML = "Hello World";
    var diseases 	= new Array();
	var i = 0;
	for (i;i<10;i++) {
		diseases[i]=0;
	}
		$( ".inline" ).each(function( index ) {
		  //console.log( index + ": " + $( this ).text() );
		  (this).innerHTML = index;
		   diseases[i] = $(this);
		   i++;
		});
    
});
