var baseUrl ="http://localhost:8000/";

// Custom JS
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      	var cookies = document.cookie.split(';');
      	for (var i = 0; i < cookies.length; i++) {
        	var cookie = jQuery.trim(cookies[i]);
        	if (cookie.substring(0, name.length + 1) == (name + '=')) {
          		cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          		return cookieValue;
        	}
      	}
    }
    return '';
}

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

	function setCookie(cname, cvalue, exdays) {
	    var d = new Date();
	    d.setTime(d.getTime() + (exdays*24*60*60*1000));
	    var expires = "expires="+ d.toUTCString();
	    document.cookie = cname + "=" + cvalue + ";" + expires+";path=/;";
	}
	