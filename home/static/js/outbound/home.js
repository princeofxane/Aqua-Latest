 $.fn.dataTable.ext.errMode = 'none';

    $('#leads_table').on( 'error.dt', function ( e, settings, techNote, message ) {
    console.log( 'An error has been reported by DataTables: ', message );
    } ) ;
      $('#calls_table1').on( 'error.dt', function ( e, settings, techNote, message ) {
    console.log( 'An error has been reported by DataTables: ', message );
    } ) ;
      $('#commits_table1').on( 'error.dt', function ( e, settings, techNote, message ) {
    console.log( 'An error has been reported by DataTables: ', message );
    } ) ;

function load_data()
{
	var emp_id;

    $('#leads_table').DataTable().destroy();
    $.ajax({
				type: "POST",
				url:"/users/getSession",
				cache: false,
				headers : { 'X_CSRFTOKEN' : getCookie('csrftoken') },
				data: {csrfmiddlewaretoken: getCookie('csrftoken') },
				success: function(data)
				{
					var parsed_response=(JSON.parse(data));
					emp_id = parsed_response.description;	
				}
			});
        $.ajax({
				type: "POST",
				url:"/outbound/getAssignedLeads",
				cache: false,
				headers : { 'X_CSRFTOKEN' : getCookie('csrftoken') },
				data: {csrfmiddlewaretoken: getCookie('csrftoken'), "emp_id":emp_id },
				success: function(data)
				{
					alert(data);	
				}
			});
    
	} 

