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

  function addtech(){
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

  function addprod(){

  

       /* var mid=$('#mid').val();;
        var mname=$('#mname').val();
        var year=$('#year').val();;
        var desc=$('#desc').val();
        var feat=$('#feat').val();

        var mrp=$('#mrp').val();
        var cat=$('#cat').val();

       var fd = new FormData();
        var files = $('#pimage')[0].files[0];
        fd.append('file',files);
        var path="http://"+ip+"/addNewProduct/"

        $.ajax({
      type: "post",
      url: path,
      processData: false,
      contentType: false,
      data: {name:mname,year:year,product_id:mid,cost:mrp,description:desc,category:cat,feature:feat,file:fd},
      success: function (data) {
        console.log(data);
        var data=JSON.parse(data);
          data=data.description;
          alert(data);        
      }
    });*/
        return false;
  }

  function addTick(){


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
   
function eRegister(){
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
      $('#emp').click(function(event){
  event.preventDefault();
        $('#cont').html('');
        $('#cont').load('/static/Addingpages/addemp.html',function(){

        	   $("#empform").on('submit', function(e) {

        e.preventDefault();
        addemployee();
       
    });

        });
 



      })


// calling add technicain function 
$('#tech').click(function(event){

	  event.preventDefault();
	   $('#cont').html('');
        $('#cont').load('/static/Addingpages/addtech.html', function() {
    $("#frmLookup").on('submit', function(e) {

        e.preventDefault();
        addtech();
       
    });








});
});




//calling add product function 

$('#prod').click(function(event){


	  event.preventDefault();
	   $('#cont').html('');
        $('#cont').load('/static/Addingpages/addprod.html',function(){

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
$('#team').click(function(event){
  event.preventDefault();
  $('#cont').load('/static/Addingpages/teamlead.html',function(){
$('#examplet').DataTable();
loadteam();
$('#myModallead').modal('show');

  });
})

//calling ticket function 

$('#tick').click(function(event){


	  event.preventDefault();
	   $('#cont').html('');
        $('#cont').load('/static/Addingpages/addtick.html',function(){
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