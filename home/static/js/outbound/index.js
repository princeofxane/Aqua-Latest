$(document).ready(function(){
		$(".iconbox").hide();
			$("#menubar").click(function(){
			$('#menubar').hide();
				$(".iconbox").show();
	});
	});

$(document).ready(function(){
		$(".close").click(function(){
		$('#menubar').show();
			$(".iconbox").hide();
});
});

$(document).ready(function(){
	
		$("#menubar").click(function(){
			$("#btn").hide();
			$(".close").click(function(){
		$('#btn').show();
});
});
});

$(document).ready(function(){
	$("#menubar").click(function(){
		$("#btn").hide();
		$(".close").click(function(){
	$('#btn').show();
});
});
});


$(document).ready(function(){
	$("#menubar").click(function(){
		$("#btn1").hide();
		$(".close").click(function(){
	$('#btn1').show();
});
});
});


$(".call-card").hide();
$("#callnow").click(function(){

	$(".call-card").show();
});

$("#goToDashboard").click(function(){
	window.location.href = baseUrl + "tc_homePage/"
});


$("#callsButton").click(function() {
	//This page is temporary
	window.location.href = baseUrl + "callHistoryPage/"
})


$("#commitsButton").click(function() {
	//This page is temporary
	window.location.href = baseUrl + "commitHistoryPage/"
})


$("#logoutButton").click(function() {
	window.location.href = baseUrl + "logoutPage/"
});

var emp_id;
var lead_id;


$(document).ready(function() {

/*	$.post( baseUrl + "getSession/",
	{},
	function(data, status) {
		dataObj=JSON.parse(data);
		if(dataObj.result=="fail") {
			window.location.href = baseUrl
		}else{*/
			emp_id =1002;
			emp_id = dataObj.description;
			getProfilePicture(emp_id);
			getUserData(emp_id);
			getCallTable(emp_id);
	/*	}
	});*/
})


function getProfilePicture(emp_id) 
{
	$.ajax({
	            type: "POST",
	            url:"/outbound/getProfilePic",
	            data: emp_id,
	            success: function(data)
	            {
	            	dataObj=JSON.parse(data);
	            	document.getElementById("imageid").src=".." + dataObj.description ;
	            }
            });
	

/*	$.post( baseUrl + "getProfilePicture/",
	{
		id: emp_id,
	},
	function(data, status) {
		dataObj=JSON.parse(data);
		if(dataObj.result=="fail") {
			alert("Something's Wrong With Profile Picture")
		}else{
			// console.log(dataObj.description);*/
			
			document.getElementById("imageid").src=".." + dataObj.description ;
	/*	}
	});*/
}

function getEmpTarget(emp_id) {
	$.post( baseUrl + "getEmpTarget/",
	{
		id: emp_id,
	},
	function(data, status) {
		dataObj=JSON.parse(data);
		if(dataObj.result=="fail") {
			// alert("Something's Wrong With Profile Picture")
		}else{
			// console.log(dataObj.description);
			document.getElementById("imageid").src=".." + dataObj.description ;
		}
	});
}




function updateCommit(lead_id,isCommit){
	$.post( baseUrl + "setCommit/",
	{
		lead_id: lead_id,
		isCommit: isCommit,
	},
	function(data, status) {
		dataObj=JSON.parse(data);
		if(dataObj.result=="fail") {
			alert("request failed")
		}else{
			// console.log(dataObj)
			// var fname = dataObj.description['fname']
			// alert("Good Job");
		}
		getCallTable(emp_id);
	});
}


function announceList(){

}
	
function setDetails(lead_id) {
	// console.log(lead_id)
	$.post(baseUrl + "editLead/",
		{
			id: lead_id,
			fname: document.getElementById("fnameLead").value,
			lname: document.getElementById("lnameLead").value,
			address: document.getElementById("addressLead").value,
			email :document.getElementById("emailLead").value,
			alternatePhone: document.getElementById("alternateNumberLead").value,
			purchaseDate: document.getElementById("dateLead").value,
			pincode: document.getElementById("pinLead").value,
			comments: document.getElementById("commentsLead").value,
		},
		function (data, status) {
			dataObj = JSON.parse(data);
			// console.log(dataObj)

			if (dataObj.result == "fail") {
				alert("request failed")
				// console.log(dataObj)
			} else {
				// console.log(dataObj)
			}
			getCallTable(emp_id);
		});
}

function callLead(lead_id)
{
// console.log(lead_id)
$.post( baseUrl + "/",
{
id : lead_id,
},
function(data, status) {
	dataObj=JSON.parse(data);
	if(dataObj.result=="fail") {
		alert("request failed")
		// console.log(dataObj)
	}else{
		// console.log(dataObj)
	}
	getCallTable(emp_id);
});
}




function getDetails(lead_id){
lead_id= lead_id
$.post( baseUrl + "displaySingleLead/",
{
	id: lead_id,
},
function(data, status) {
	dataObj=JSON.parse(data);
	if(dataObj.result=="fail") {
		alert("request failed")
	}else{
		// console.log(dataObj)
		document.getElementById("lead_id").innerText = lead_id;
		document.getElementById("lead_phone").innerText = dataObj.description['mobile'];
		document.getElementById("fnameLead").value = dataObj.description['fname'];
		document.getElementById("lnameLead").value = dataObj.description['lname'];
		document.getElementById("emailLead").value = dataObj.description['email'];
		document.getElementById("alternateNumberLead").value = dataObj.description['alternatePhone'];
		document.getElementById("pinLead").value = dataObj.description['pincode'];
		document.getElementById("dateLead").value = dataObj.description['purchaseDate'];
		document.getElementById("addressLead").value = dataObj.description['address'];
		// document.getElementById("commentsLead").value = dataObj.description['comments'];
		latest = '';
		let i=0;
		comments = dataObj.description['comments'];
		if(comments == '' || comments == null){
			latest = '';				
		}
		else{
			for (let i = 0; i < comments.length; i++) {
				if(comments[i] == '#'){
					latest = latest + "\n";
					continue;
				}
				latest=latest+comments[i];
			}
		}
		document.getElementById("commentsList").innerText = latest;
		document.getElementById("btnLead").setAttribute('onclick','setDetails('+lead_id+')')
	}
	getCallTable(emp_id);
});
}



function getUserData(emp_id) {
	$.post( baseUrl + "getUserData/",
	{
		id: emp_id,
	},
	function(data, status) {
		dataObj=JSON.parse(data);
		if(dataObj.result=="fail") {
			alert("request failed")
		}else{
			// console.log(dataObj)
			var fname = dataObj.description['fname']
			var lname = dataObj.description['lname']
			loginTime = dataObj.description['loginTime']
			var d = new Date(loginTime);

			var date = d.getMonth() + 1

			$("#loginTime").text('Logged in at: ' + d.getHours() + ' : ' + d.getMinutes())
			$("#loginDate").text('Date: ' + d.getDate() + '-' + date + '-' + d.getFullYear())

			fullName = makeItUpper(fname, lname)
			$("#welcomeTag").text("Hello " + fullName);
			//To a change welcome
		}
		// getCallTable(emp_id)
	});
}


function getCallTable(emp_id) {
document.getElementById('main-table').innerHTML=' ';
$.post( baseUrl + "getAssignedLeads/",
{
	id: emp_id,
},
function(data, status){
	dataObj = JSON.parse(data);
	if(dataObj.result == 'fail') {
		alert("Sorry No Data Assigned Yet");
	}else{
		// for (var i=0; i < dataObj.description.length; i++) {
		// 	console.log(dataObj.description[i]['fname'])
		// }
		var columns = addAllColumnHeaders(dataObj.description);
		for (var i = 0 ; i < dataObj.description.length ; i++) {
			var row$ = $('<tr/>');
			for (var colIndex = 0 ; colIndex < columns.length ; colIndex++) {
				var cellValue = dataObj.description[i][columns[colIndex]];
				if(typeof cellValue === "boolean"){
					lead_id = dataObj.description[i][columns[0]];
					if(cellValue == false){
						row$.append($('<td/>').html('<input type="button" class="btn" onclick="updateCommit('+lead_id+','+'1'+')" value="Commit">'));
						row$.append($('<td/>').html('<input type="button" class="btn" data-toggle="modal" data-target="#myModal" onclick="getDetails('+lead_id+')" value="Details">'));
						row$.append($('<td/>').html('<input type="button" class="btn" onclick="callLead('+lead_id+')" value="Call Now">'));
					}
					else if(cellValue == true){
						row$.append($('<td/>').html('<input type="button" class="btn" onclick="updateCommit('+lead_id+',)"value="Un Commit">'));
						row$.append($('<td/>').html('<input type="button" class="btn" data-toggle="modal" data-target="#myModal" onclick="getDetails('+lead_id+')" value="Details">'));
						row$.append($('<td/>').html('<input type="button" class="btn" onclick="callLead('+lead_id+')" value="Call Now">'));
					}
				}
				else if (colIndex == 5) {
					// cellValue="hey";
					cellValue = dataObj.description[i][columns[colIndex]];
					// console.log(cellValue);
					var latest = '';
					if(cellValue == '' || cellValue == null){
						row$.append($('<td/>').html(cellValue));
					}
					else{
						for (let i = 0; i < cellValue.length; i++) {
							if(cellValue[i] == '#'){
								break;
							}
							latest=latest+cellValue[i];
						}
						row$.append($('<td/>').html(latest));	
					}
					
				}
				else
				{
					if (cellValue == null) { 
						cellValue = ""; 
					}
						//arrange header
						// var orderedCellValue = orderCells(cellValue);
					row$.append($('<td/>').html(cellValue));
				}
			}
			$("#main-table").append(row$);
			// row$.append($('<td/>').html('<button type="button" class="btn btn-secondary callButton">CallNow</button>'));
			// row$.append($('<td/>').html('<button type="button" id='+dataObj.description[i][columns[0]]+' class="btn" onclick="upgateCommit('+dataObj.description[i][columns[7]]+')">Set Commit</button>'));
			// row$.append($('<td/>').html('<button type="button" class="btn btn-secondary callButton">CallNow</button>'));
			// row$.append($('<td/>').html('<button type="button" class="btn"data-toggle="modal" data-target="#myModal">Details</button>'));
			// row$.append($('<td/>').html('<input type="button" class="btn" onclick="updateCommit('+dataObj.description[i][columns[0]]+',)"value="Un Commit">'));

		}
	}
});
}
	// $('#excelDataTable').DataTable();

function orderCells(headers) {
	for (var header of headers) {
		// console.log(header)
	}
}

function getNotificationsTable() {
document.getElementById('main-table').innerHTML='';
$.post( baseUrl + "getNotification/",
{
	id: emp_id,
},
function(data, status){
	dataObj = JSON.parse(data);
	if(dataObj.result == 'fail') {
		alert(dataObj.description);
	}else{
		// for (var i=0; i < dataObj.description.length; i++) {
		// 	console.log(dataObj.description[i]['fname'])
		// }
		$("#main-table").append('--');				
		$("#main-table").append('Messages Only For You');
		$("#main-table").append('----------------------');				

		var columns = addAllColumnHeaders(dataObj.description);
		for (var i = 0 ; i < dataObj.description.length ; i++) {
			var row$ = $('<tr/>');
			for (var colIndex = 0 ; colIndex < columns.length ; colIndex++) {
				var cellValue = dataObj.description[i][columns[colIndex]];
				if(typeof cellValue === "boolean"){
					lead_id = dataObj.description[i][columns[0]];
				}
				else{
					if (cellValue == null) { 
						cellValue = ""; 
					}
					row$.append($('<td/>').html(cellValue));
				}
			}
			$("#main-table").append(row$);
		}
	}
});

$.post( baseUrl + "getNotification/",
{},
function(data, status){
	dataObj = JSON.parse(data);
	if(dataObj.result == 'fail') {
		alert(dataObj.description);
	}else{
		// console.log(data);
		// for (var i=0; i < dataObj.description.length; i++) {
		// 	console.log(dataObj.description[i]['fname'])
		// }
		$("#main-table").append('--');				
		$("#main-table").append('Messages For All');				
		$("#main-table").append('----------------------');				

		var columns = addAllColumnHeaders(dataObj.description);
		for (var i = 0 ; i < dataObj.description.length ; i++) {
			var row$ = $('<tr/>');
			for (var colIndex = 0 ; colIndex < columns.length ; colIndex++) {
				var cellValue = dataObj.description[i][columns[colIndex]];
				if(typeof cellValue === "boolean"){
					lead_id = dataObj.description[i][columns[0]];
				}
				else{
					if (cellValue == null) { 
						cellValue = ""; 
					}
					row$.append($('<td/>').html(cellValue));
				}
			}
			$("#main-table").append(row$);
		}
	}
});

}


function addAllColumnHeaders(myList) {
	var columnSet = [];
	var headerTr$ = $('<tr/>');
	for (var i = 0 ; i < dataObj.description.length ; i++) {
		var rowHash = dataObj.description[i];
		for (var key in rowHash) {
			if ($.inArray(key, columnSet) == -1){
				columnSet.push(key);
				headerTr$.append($('<th />').html(key));
			}
		}
	}
	headerTr$.append($('<th />').html(' '));
	$("#main-table").append(headerTr$);

	return columnSet;
} 

$(document).ready(function() {
	setInterval(function() {

		var d = new Date(loginTime);
		var login = d.getMinutes()*60 + d.getHours()*60*60 + d.getSeconds()
		var c = new Date();
		var curDate = c.getMinutes()*60 + c.getHours()*60*60 + c.getSeconds()

		a = Number(curDate -login);
		var h = Math.floor(a / 3600);
		var m = Math.floor(a % 3600 / 60);
		var s = Math.floor(a % 3600 % 60);

		// var hDisplay = h > 0 ? h + (h == 1 ? " hour, " : " hours, ") : "";
		// var mDisplay = m > 0 ? m + (m == 1 ? " minute, " : " minutes, ") : "";
		// var sDisplay = s > 0 ? s + (s == 1 ? " second" : " seconds") : "";

		var hDisplay = h > 0 ? h + (h == 1 ? " hour, " : " hours, ") : "";
		var mDisplay = m > 0 ? m + (m == 1 ? " minute, " : " minutes, ") : "";
		var sDisplay = s > 0 ? s + (s == 1 ? " second" : " seconds") : "";
		$("#runningTime").text(h + ":" + m + "." + s)
	// $("#runningTime").text(d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12:true }))
	}, 1000)
})

// startTimer();

$("#pauseButton").click(function(e) {
	e.preventDefault();
	$('#modalForPause').modal('show');
	startCounter();
	$.post( baseUrl + "setPause/",
	{
		id: emp_id,
		isPause: true
	},
	function(data, status) {
		dataObj = JSON.parse(data);
		if(dataObj.result == 'fail') {
			alert(dataObj.description)
		}else {
			console.log(dataObj.description)
		}

	})
});

$('#resume').click(function(e){
	e.preventDefault();
	// location.reload();
	resetCounter();
	$("#modalForPause").modal("hide");
	$.post(baseUrl + "setPause/",
	{
		id:emp_id,
		isPause: false
	},
	function(data, status) {
		dataObj = JSON.parse(data);
		if(dataObj.result == 'fail') {
			alert(dataObj.description)
		}else {
			pauseDuration = dataObj.description
		}
	})

});

