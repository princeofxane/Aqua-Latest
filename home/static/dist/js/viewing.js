 
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
        $('#cont').load('/static/viewpage/prodview.html',function(){
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
        $('#cont').load('/static/viewpage/techview.html',function(){
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
        $('#cont').load('/static/viewpage/tickview.html',function(){

          var table=$('#example5').DataTable();
          callip(4);

  

        });
 



      })




       $('#cwork').click(function(event){


  event.preventDefault();
        $('#cont').html('');
        $('#cont').load('/static/viewpage/viewingbooking.html',function(){
          $('#examplework').DataTable();
          callip(5);


        });
 



      })



        $('#prebook').click(function(event){


  event.preventDefault();
        $('#cont').html('');
        $('#cont').load('/static/viewpage/previousbook.html',function(){
          $('#examplepre').DataTable();
          callip(6);


        });
 



      })

     

    });