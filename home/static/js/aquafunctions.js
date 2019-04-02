  var ip;


function initialize() {
//  alert("xool");

var input = document.getElementById('address');
var autocomplete = new google.maps.places.Autocomplete(input);
google.maps.event.addListener(autocomplete, 'place_changed', function () {
var place = autocomplete.getPlace();
document.getElementById('city2').value = place.name;
document.getElementById('cityLat').value = place.geometry.location.lat();
document.getElementById('cityLng').value = place.geometry.location.lng();
});
}

//This is for adding employee
function addemployee(){
 var fi_name=$('#fname').val();;
  var email=$('#inputEmail3').val();;
  var phone1=$('#phone').val();
  var path="http://"+ip+"/registerEmployee/";

  $.ajax({
type: "post",
url: path,
data: {fname:fi_name,mail:email,phone:phone1},
success: function (data) {
  console.log(data);
  var data=JSON.parse(data);
    data=data.description;
    alert(data);        
}
});
return false;
}

function tassign(id){
$('#eid').val(id);
$('#myModallead').modal('show');

}

function loadteam(){
var path="http://"+ip+"/displayCurrentBookings/";
var table =   $('#examplet').DataTable();
              table.clear().draw();

      $.ajax({
type: "GET",
url: path,
data: {},
success: function (data) {
  var data=JSON.parse(data);
  data=data.description;
  console.log(data);

$.each(data, function(key,value) {
table.row.add($(
'<tr>' +
'<td>'+value.customerName+'</td>' +
'<td>'+value.problem+'</td>' +
'<td>'+value.customerPincode+'</td>' +
'<td>'+value.Customerplace+'</td>' +
'<td>'+value.assigned+'</td>' +

'<td><input type="submit" id="'+value.id+'" onclick="tassign(this.id)" value="Assign now" class="btn btn-warning"></td>' +


'</tr>'
)).draw(false);

  }); 

},
error:function(data){
  console.log(data);
}
});
}


//This is for adding technician
function addtech()
{
 var name=$('#name').val();;
  var phone=$('#phone').val();
  var pass=$('#pass').val();;
  var pin=$('#pin').val();
  var mail=$('#mail').val();
  var path="http://"+ip+"/registerTechnician/";


  $.ajax({
type: "post",
url: path,
data: {username:name,pincode:pin,password:pass,phone:phone,mail:mail},
success: function (data) {
  console.log(data);
  var data=JSON.parse(data);
    data=data.description;
    alert(data);        
}
});
return false;
}


function addprod()
{
  return false;
}

function addTick()
{


   path="http://"+ip+"/registerTicket/"

      var fname=$('#fname').val();;
      var lname=$('#lname').val();
      var mail=$('#mail').val();;
      var alter=$('#alter').val();
      var phone=$('#phone').val();
      var address=$('#address').val();
      var dev=$('#dev').val();
      var pin=$('#pin').val();
      var prob=$('#prob').val();
      var land=$('#land').val();
      var city=$('#city2').val();
      var cityLat=$('#cityLat').val();
      var cityLng=$('#cityLng').val();

   

      $.ajax({
    type: "post",
    url: path,
    data:{fname:fname,device:dev,lname:lname,email:mail,phone:phone,alter:alter,problem:prob,pincode:pin,address:address,land:land,city:city,cityLat:cityLat,cityLng:cityLng},
    success: function (data) {
      console.log(data);
      var data=JSON.parse(data);
      if(data.result != "success"){
        alert("sorry no technician found so please do find some other way");
      }
      else{

        data=data.description;
        $('#name1').val(data['name']);
        $('#mail2').val(data['mail']);
        $('#phone2').val(data['phone']);
        $('#pin2').val(data['pin']);
        $('#myModal2').modal('show');   
        $('#form1')[0].reset();    
      }
    }
  });


}
//calling phone search

  function phoneCheck(){
  if($('#phone').val().length == 10){
  path="http://"+ip+"/checkPhone/"

  var phone=$('#phone').val();
  $.ajax({
  type: "post",
  url: path,
  data:{phone:phone},
  success: function (data) {
  console.log(data);
  var data=JSON.parse(data);
  if(data.result=="success"){
  data=data.description;
  $('#phone1').val(data['phone']);
  $('#mail1').val(data['email']);
  $('#fname1').val(data['lname']);
  $('#lname1').val(data['fname']);
  $('#address1').val(data['address']);
  $('#dev1').val(data['product_id']);
  $('#pin1').val(data['pincode']);
  $('#app').html(data['product_name']);
  $('#alter1').val(data['alternativeMobile']);
  $('#land1').val(data['land']);
  $('#cid').val(data['id']);
  $('#city3').val(data['city']);
  $('#cityLat2').val(data['latitude']);
  $('#cityLng2').val(data['longitude']);

  $('#myModal').modal('show');
  }
  }
  });


  }
  }
   
function eRegister()
{
    var prob=$('#prob1').val();
    var cid=$('#cid').val();

    path="http://"+ip+"/registerTicketExist/"

    $.ajax({
    type: "post",
    url: path,
    data:{problem:prob,cid:cid},
    success: function (data) {
    console.log(data);
    var data=JSON.parse(data);
    if(data.result != "success"){
    alert("sorry no technician found so please do find some other way");
    }
    else{

    data=data.description;
    $('#name1').val(data['name']);
    $('#mail2').val(data['mail']);
    $('#phone2').val(data['phone']);
    $('#pin2').val(data['pin']);
    $('#form2')[0].reset();
    $('#myModal2').modal('show');   
    $('#myModal').modal('hide');
    }
    }
    });
}

function call(){
  path="http://"+ip+"/displayAllDevice/"

       $.ajax({
      type: "get",
      url: path,
      data:{},
     // data: {name:name,address:add,devicename:dev,pincode:pin,problem_description:prob},
      success: function (data) {
        console.log(data);
        var data=JSON.parse(data);
          data=data.description;
          $.each(data,function(key,value){
$('<option>').val(value.product_id).text(value.name).appendTo('#products');
          });       
      }
    });
     }

 function checkMail(){
 	    if($('#mail').val() !=''){
        path="http://"+ip+"/checkMail/"
        var mail=$('#mail').val();
            $.ajax({
      type: "post",
      url: path,
      data:{mail:mail},
      success: function (data) {
        console.log(data);
        var data=JSON.parse(data);
        if(data.result=="success"){
          data=data.description;
          $('#phone1').val(data['phone']);
          $('#mail1').val(data['email']);
          $('#fname1').val(data['lname']);
          $('#lname1').val(data['fname']);
          $('#address1').val(data['address']);
          $('#dev1').val(data['product_id']);
          $('#pin1').val(data['pincode']);
          $('#app').html(data['product_name']);
          $('#alter1').val(data['alternativeMobile']);
          $('#land1').val(data['land']);
             $('#cid').val(data['id']);
             $('#city3').val(data['city']);
          $('#cityLat2').val(data['latitude']);
          $('#cityLng2').val(data['longitude']);

$('#myModal').modal('show');
}
      }
    });

      }
 }

$(document).ready(function(){

//calling add employee function 
/*$('#emp').click(function(event){
event.preventDefault();
$('#cont').html('');
$('#cont').load('/static/Addingpages/addemp.html',function(){
$("#empform").on('submit', function(e) {
e.preventDefault();
addemployee();
});
});
})*/


// calling add technicain function 
/*$('#tech').click(function(event){
event.preventDefault();
$('#cont').html('');
$('#cont').load('/static/Addingpages/addtech.html', function() {
$("#frmLookup").on('submit', function(e) {
e.preventDefault();
addtech();

});
});
});
*/


//calling add product function 

$('#prod').click(function(event){


	  event.preventDefault();
	   $('#cont').html('');
        $('#cont').load('addprod/',function(){

           $('#myprod').ajaxForm(function(data) {
            //alert("dafad");

          console.log(data);
        var data=JSON.parse(data);
          data=data.description;
          var id;
          id=data.id;
          $("#loadimg").attr('src',"/static/qrcode/"+id+".svg");
          $('#myModalimg').modal('show');


            }); 
/*
        	$('#myprod').submit(function(e){
        		e.preventDefault();
        		addprod();

        	})*/

        });

});
/*$('#team').click(function(event){
  event.preventDefault();
  $('#cont').load('ib_teamlead/',function(){
$('#examplet').DataTable();
loadteam();
$('#myModallead').modal('show');

  });
})*/

//calling ticket function 

$('#tick').click(function(event){


	  event.preventDefault();
	   $('#cont').html('');
        $('#cont').load('addtick/',function(){
        		call();


        	$('#form1').submit(function(e){
        	e.preventDefault();
        	addTick();
        });



        	    $('#phone').keyup(function(e){
    	        e.preventDefault();

   //calling the phone api response
   if($('#phone').val().length==10){
   phoneCheck();
 }
  })


$('#alter').keyup(function(){
  if($('#alter').val().length==1){
  checkMail();
}
    });




$('#add1').click(function(e){
     e.preventDefault();

      eRegister();


    });




        });

});

     $.ajax({
    type: "post",
    url: "/static/var1.json",
    dataType: "json",
    success: function(data) {
      console.log(data);
     // data=JSON.parse(data);
     data=data.data1;
      // url=data['ip'];

      ip=data['ip'];


    },
    error: function(){
        alert("json not found");
    }
});
           
 
 

     })








var ip;
var tid=[];
var tname=[];
var boolval=0;

//to edit the value of the exisiting employee

  function loadpre(){
                      var table=$('#examplepre').DataTable();
                      table.clear().draw();


    var path="http://"+ip+"/displayPreviousBookingAdmin/";
        $.ajax({
      type: "post",
      url: path,
      data: {},
      success: function (data) {
          var data=JSON.parse(data);
          data=data.description;
          console.log(data);

        $.each(data, function(key,value) {
      table.row.add($(
    '<tr>' +
    '<td id="'+value.id+'">'+value.id+'</td>' +

    '<td id="'+value.id+'">'+value.client_name+'</td>' +
    

    '<td id="'+value.id+'">'+value.area+'</td>' +
    '<td id="'+value.id+'">'+value.pincode+'</td>' +
'<td id="'+value.id+'">'+value.phone+'</td>' +
    '<td id="'+value.id+'">'+value.alternate_phone+'</td>' +

    '<td id="'+value.id+'">'+value.problem+'</td>' +

    '<td id="'+value.id+'">'+value.cost+'</td>' +

   



    '</tr>'
)).draw(false);
    
    
          }); 
        
        },
        error:function(data){
          console.log(data);
        }
        });
 }







function finalbook(id){
  var tid=$('#s'+id).val();
  path="http://"+ip+"/assignTechnicianToCurrentBooking/";
   $.ajax({
      type: "post",
      url: path,
      data: {tid:tid,cid:id},
      success: function (data) {
          var data=JSON.parse(data);
          data=data.description;
          alert(data);
        }
      });




}



function loadall(){

  var path="http://"+ip+"/displayAllAssignedTickets/";

  var table =   $('#exampleworkdone').DataTable();
                      table.clear().draw();
              $.ajax({
      type: "get",
      url: path,
      data: {},
      success: function (data) {
          var data=JSON.parse(data);
          data=data.description;
          console.log(data);

        $.each(data, function(key,value) {
      table.row.add($(

    '<tr>' +

    '<td >'+value.technician+'</td>' +

    '<td >'+value.customer+'</td>' +
    

    '<td >'+value.problem+'</td>' +
        '<td >'+value.pincode+'</td>' +




    '</tr>'
)).draw(false);
        
          }); 
        
        },
        error:function(data){
          console.log(data);
        }
        });
}



function loadworks(){
  
  var path="http://"+ip+"/displayTodaysBooking1/";

  var table =   $('#examplework').DataTable();
                      table.clear().draw();
              $.ajax({
      type: "post",
      url: path,
      data: {},
      success: function (data) {
          var data=JSON.parse(data);
          data=data.description;
          console.log(data);

        $.each(data, function(key,value) {
      table.row.add($(

    '<tr>' +

    '<td id="'+value.id+'">'+value.problem+'</td>' +

    '<td id="f'+value.id+'">'+value.client_name+'</td>' +
    

    '<td id="p'+value.id+'">'+value.pincode+'</td>' +
    '<td id="ph'+value.id+'"><select class="form-control" id="s'+value.id+'"></select></td>' +


    '<td><input type="submit" id="'+value.id+'" onclick="finalbook(this.id)" style="margin-bottom:3px;" value="Assign" class="btn btn-success"></td>'+



    '</tr>'
)).draw(false);
        
          });



        $.each(data,function(key,value){
          console.log("this is the each loop");


            var select = $('#s'+value.id);
            console.log("this is the eroor"+value.id);

    select.empty();

    select.append("<option value=''>---Select your technician---</option>");


    for (var i = 0; i < tid.length; i++){
      console.log("for looop");
          var length = $('#s'+value.id).children('option').length;

            console.log(tid[i]+ "--" + tname[i]);
            $("#s"+value.id).append("<option value='" +tid[i]+ "'>" +tname[i]+ "</option>");

          }


         /* for(i=0;i<tid.length;i++){
              $("<option/>").val(tid[i]).text(tname[i]).appendTo("#s"+value.id);



          } */

        });
      
      boolval++;
        
        },
        error:function(data){
          console.log(data);
        }
        });
}

function apiEdit(){
  var fi_name=$('#fname').val();;
        var la_name=$('#lname').val();
        var email=$('#inputEmail3').val();;
        var phone1=$('#phone').val();
        var path="http://"+ip+"/editEmployee/"
        var id=$('#eid').val();

        $.ajax({
      type: "post",
      url: path,
      data: {fname:fi_name,lname:la_name,mail:email,phone:phone1,id:id},
      success: function (data) {
        console.log(data);
        var data=JSON.parse(data);
          data=data.description;
          alert(data);
          loademp();        
      }
    });
    return false;


}

function apiTechEdit(){

  var name=$('#name').val();;
        var phone=$('#phone').val();
        var id=$('#tid').val();;
        var pin=$('#pin').val();
        var path="http://"+ip+"/editTechnician/";


        $.ajax({
      type: "post",
      url: path,
      data: {username:name,pincode:pin,id:id,phone:phone},
      success: function (data) {
        console.log(data);
        var data=JSON.parse(data);
          data=data.description;
          alert(data); 
            
          loadtech();  
      }
    });
    return false;



}

function apiProdEdit(){

  var mid=$('#mid').val();
  var mname=$('#mname').val();
  var year=$('#year').val();
  var desc=$('#desc').val();
  var feat=$('#feat').val();
  var mrp=$('#mrp').val();
  var cat=$('#cat').val();
  var id=$('#fid').val();

var path="http://"+ip+"/editProduct/"

    $.ajax({
      type: "post",
      url: path,
      data: {id:id,product_id:mid,name:mname,year:year,cost:mrp,description:desc,category:cat,feature:feat},
      success: function (data) {
        console.log(data);
        var data=JSON.parse(data);
          data=data.description;
          alert(data); 

            
          loadprod();     
      }
    });
    return false;



}

//editing the technician 
function techedit(id){
  $('#name').val($('#f'+id).text());;
  $('#phone').val($('#ph'+id).text());
  $('#pin').val($('#p'+id).text());
  $('#tid').val(id);
        $('#myModaltech').modal('show');
}


//editing the ticket
function tickedit(id){
          $('#myModaltick').modal('show');
}

//edit the product
function prodedit(id){

  $('#mid').val($('#p'+id).text());
  $('#mname').val($('#pname'+id).text());
  $('#year').val($('#year'+id).text());
  $('#desc').val($('#desc'+id).text());
  $('#feat').val($('#cat'+id).text());
  $('#mrp').val($('#cost'+id).text());
  $('#cat').val($('#cat'+id).text());
  $('#fid').val(id);


  $('#myModalprod').modal('show');
}


//editing the employee
function empedit(id){
   $('#fname').val($('#f'+id).text());
        $('#lname').val($('#l'+id).text());
        $('#inputEmail3').val($('#e'+id).text());
        $('#phone').val($('#p'+id).text());
        $('#eid').val(id);


  $('#myModalemp').modal('show');
}


//loading the ticket view 

function loadtick(){
var path="http://"+ip+"/displayAllTickets/"
var table =   $('#example5').DataTable();
table.clear().draw();

$.ajax({
type: "GET",
url: path,
data: {},
success: function (data) {
var data=JSON.parse(data);
data=data.description;
console.log(data);

$.each(data, function(key,value) {
table.row.add($(
'<tr>' +
'<td>'+value.phone+'</td>' +
'<td>'+value.mail+'</td>' +
'<td>'+value.pin+'</td>' +
'<td>'+value.prob+'</td>' +
'<td>'+value.date+'</td>' +

'<td><input type="submit" id="'+value.id+'" onclick="tickedit(this.id)" style="margin-bottom:3px;" value="edit" class="btn btn-success"></td>'+
'<td><input type="submit" id="'+value.id+'" onclick="tidel(this.id)" value="Dismiss" class="btn btn-warning"></td>' +


'</tr>'
)).draw(false);

}); 

},
error:function(data){
console.log(data);
}
});
}


//loading the technician
function loadtech(){
if(boolval==0){
}

var path="http://"+ip+"/displayEmployee/";

var table =   $('#example4').DataTable();
table.clear().draw();
$.ajax({
type: "get",
url: path,
data: {},
success: function (data) {
var data=JSON.parse(data);
data=data.description;
console.log(data);

$.each(data, function(key,value) {
if(value.category=="tn"){
var cat="Technican";
tid.push(value.id);
tname.push(value.name);
table.row.add($(
'<tr>' +
'<td id="'+value.id+'">'+value.id+'</td>' +

'<td id="f'+value.id+'">'+value.name+'</td>' +


'<td id="p'+value.id+'">'+value.pincode+'</td>' +
'<td id="ph'+value.id+'">'+value.phone+'</td>' +


'<td><input type="submit" id="'+value.id+'" onclick="techedit(this.id)" style="margin-bottom:3px;" value="edit" class="btn btn-success"></td>'+
'<td><input type="submit" id="'+value.id+'" onclick="tdel(this.id)" value="Dismiss" class="btn btn-warning"></td>' +



'</tr>'
)).draw(false);
}

}); 

},
error:function(data){
console.log(data);
}
});
}


//deleting the product

function pdel(id){
path="http://"+ip+"/deleteDevice/";
$.ajax({
type: 'post',
url: path,
data: {product_id:id},
success: function (data) {
var data=JSON.parse(data);
console.log(data);

alert(data.description);
loadprod();
}
});
}


//loading the product


function loadprod(){

var table=$('#example3').DataTable();
table.clear().draw();

var path="http://"+ip+"/displayAllDevice/";

$.ajax({
type: "GET",
url: path,
data: {},
success: function (data) {
var data=JSON.parse(data);
data=data.description;
console.log(data);
$.each(data, function(key,value) {
table.row.add($(
'<tr>' +
'<td id="p'+value.id+'">'+value.product_id+'</td>' +
'<td id="pname'+value.id+'">'+value.name+'</td>' +
'<td id="year'+value.id+'">'+value.year+'</td>' +
'<td id="desc'+value.id+'">'+value.description+'</td>' +
'<td id="feat'+value.id+'">'+value.feature+'</td>' +
'<td id="cat'+value.id+'">'+value.category+'</td>' +
'<td id="cost'+value.id+'">'+value.cost+'</td>' +


'<td><input type="submit" id="'+value.id+'" onclick="prodedit(this.id)" style="margin-bottom:3px;" value="edit" class="btn btn-success"></td>'+
'<td><input type="submit" id="'+value.id+'" onclick="pdel(this.id)" value="delete" class="btn btn-warning"></td>' +



'</tr>'
)).draw(false);

}); 

},
error:function(data){
console.log(data);
}
});
}


//loading the employee

function loademp(){
var table=$('#example2').DataTable();
table.clear().draw();


var path="http://"+ip+"/displayEmployee/";
$.ajax({
type: "get",
url: path,
data: {},
success: function (data) {
var data=JSON.parse(data);
data=data.description;
console.log(data);

$.each(data, function(key,value) {
if(value.category=="tc"){
var cat="Tele caller";
table.row.add($(
'<tr>' +
'<td id="'+value.id+'">'+value.id+'</td>' +

'<td id="f'+value.id+'">'+value.name+'</td>' +


'<td id="e'+value.id+'">'+value.email+'</td>' +
'<td id="p'+value.id+'">'+value.phone+'</td>' +


'<td><input type="submit" id="'+value.id+'" onclick="empedit(this.id)" style="margin-bottom:3px;" value="edit" class="btn btn-success"></td>'+
'<td><input type="submit" id="'+value.id+'" onclick="edel(this.id)" value="Dismiss" class="btn btn-warning"></td>' +



'</tr>'
)).draw(false);
}

}); 

},
error:function(data){
console.log(data);
}
});
}


//loading call ip and it will get the ip address

function callip(rtype){
console.log("IP");

$.ajax({
type: "post",
url: "/static/var1.json",
dataType: "json",
success: function(data) {
console.log(data);
// data=JSON.parse(data);
data=data.data1;
// url=data['ip'];

ip=data['ip'];
if(rtype==1){
loademp();
}
else if(rtype==2){
loadtech();
}
else if(rtype==3){
loadprod();
}
else if(rtype==4){
loadtick();
}
else if(rtype==5){

tid=[];
tname=[];

loadtech();

loadall();
console.log(tid);
loadworks();
boolval++;
}
else if(rtype==6){
loadpre();
}




},
error: function(){
alert("json not found");
}
});
}

//this is to delete the employee
function edel(id){
var path="http://"+ip+"/deactivateEmployee/"
$.ajax({
type: 'post',
url: path,
data: {employee_id:id},
success: function (data) {
var data=JSON.parse(data);
console.log(data);

alert(data.description);
loademp();
}
});
}

//deleting technicain 

function tdel(id){
var path="http://"+ip+"/deactivateEmployee/"
$.ajax({
type: 'post',
url: path,
data: {employee_id:id},
success: function (data) {
var data=JSON.parse(data);
console.log(data);

alert(data.description);
loadtech();
}
});
}


$(document).ready(function(){

//calling add employee function 
$('#empview').click(function(event){


event.preventDefault();
$('#cont').html('');
$('#cont').load('/static/viewpage/empview.html',function(){

var table=$('#example2').DataTable();
callip(1);
$('#editempbtn').click(function(event){
event.preventDefault();

apiEdit();
})




});




})



// calling product view page

$('#prodview').click(function(event){


event.preventDefault();
$('#cont').html('');
$('#cont').load('prodview/',function(){
var table=$('#example3').DataTable();
callip(3);
$('#editprod1').click(function(event){
event.preventDefault();
apiProdEdit();
$('#myModalprod').modal('hide');   

})


});




})


// calling technician view page


$('#techview').click(function(event){


event.preventDefault();
$('#cont').html('');
$('#cont').load('techview/',function(){
var table=$('#example4').DataTable();
callip(2);
$('#edittech').click(function(event){
event.preventDefault();
apiTechEdit();

})


});




})
//calling ticket view function 


$('#tickview').click(function(event){


event.preventDefault();
$('#cont').html('');
$('#cont').load('tickview/',function(){

var table=$('#example5').DataTable();
callip(4);



});




})




$('#cwork').click(function(event){


event.preventDefault();
$('#cont').html('');
$('#cont').load('viewingbooking/',function(){
$('#examplework').DataTable();
callip(5);


});




})



$('#prebook').click(function(event){


event.preventDefault();
$('#cont').html('');
$('#cont').load('previousbook/',function(){
$('#examplepre').DataTable();
callip(6);


});




})



});





  //___________________________________________________________________________________________________________


  //Firebase



var ip;
var idlist=[];
var sta=[];
var myval;
var allid=[];

function fload(){
var db = firebase.database().ref();
db.on("value",snap=>{
var data=snap.val();
$('#currentbook').click();
console.log(data);
});
}


function changeval(id){
var idval=$('#id'+id).text();
$('#fid').val(id);
$('#bid').val(idval);
$('#myModalsal').modal('show');

}

$(document).ready(function(){
var bval=0;
if(bval>0){
fload();
}


$('#currentbook').click(function(event){

event.preventDefault();
$('#cont').html('');
$('#cont').load('currentbookview/',function(){
bval++;
if(bval==1){
fload();
}

  



          //to load the ip address of the current working server

         $.ajax({
    type: "post",
    url: "/static/var1.json",
    dataType: "json",
    success: function(data) {
      console.log(data);
     // data=JSON.parse(data);
     data=data.data1;
      // url=data['ip'];

      ip=data['ip'];




//to load the firebase value to the array and send


idlist=[];
var db = firebase.database().ref("technician");
db.on('value',snap=>{
myval=snap.val();
console.log("the value"+myval);

idlist=[];
sta=[];
allid=[];
$.each(myval, function(key,value) {
console.log("the key value is"+key);
console.log(value);
idlist.push(value.currentBookingId);
sta.push(value.status);
allid.push(key);

});

console.log(idlist);

console.log(sta);

});


//this is to assing the values
var table=$('#examplesta').DataTable();
table.clear().draw();
 for(j=0;j<sta.length;j++)
 {
  staval=parseInt(sta[j]);
  if(staval==1 || staval==2 || staval==3)
  {
    var path="http://"+ip+"/fetchDetailsFromBookingId/";
    var idToString=JSON.stringify(idlist);
    $.ajax({
      type: "post",
      url: path,
      data: {id:idToString},
      success: function (data) {
          var data=JSON.parse(data);
          data=data.description;
          console.log(data);
          i=0;
          //0 is waiting 1 is on way 2 is working 3 is requesting payment
          $.each(data, function(key,value) {
          if(staval==1 || staval==2 || staval==3){
          var currentstatus;
        if(staval==1 || staval==2 || staval==3){
          if(staval==0){
            currentstatus="waiting";

          }
          else if(staval==1){
            currentstatus="on the way";
          }
          else if(staval==2){
            currentstatus="working";
          }
          else if(staval==3){
            currentstatus="request payment";
          }
table.row.add($(
'<tr id="'+allid[i]+'" onclick="changeval(this.id)">' +
'<td id="id'+allid[i]+'">'+value.id+'</td>' +
'<td id="'+allid[i]+'">'+value.customer+'</td>' +
'<td id="f'+allid[i]+'">'+value.technician+'</td>' +
'<td id="e'+allid[i]+'">'+value.pincode+'</td>' +
'<td id="e'+allid[i]+'">'+currentstatus+'</td>' +
'</tr>'
)).draw(false);
}
}

i++;
}); 
},
error:function(data){
console.log(data);
}
});
}
}
},
error: function(){
alert("json not found");
}
});                   

        

$('#salsal').click(function(event){
event.preventDefault();
$('#myModalsal').modal('hide');
var fid=$('#fid').val();
var bid=$('#bid').val();
var amount=$("#amount").val();
console.log(fid+" "+bid);
myval[fid].pay=parseInt(amount);
myval[fid].status=4;
var a=firebase.database().ref("technician/");
a.set(myval);
var path="http://"+ip+"/serviceCompleted/"
$.ajax({
type: "post",
url: path,
data: {serviceId:bid,cost:amount},
success: function (data) {
var data=JSON.parse(data);
data=data.description;
location.reload();
console.log(data);
}
});
})
});
})
})