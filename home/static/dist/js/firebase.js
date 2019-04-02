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
        $('#cont').load('/static/viewpage/currentbookview.html',function(){
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
		/*myval['1000'].pay=5000;
		console.log(myval['1000'].pay);
		var a=firebase.database().ref("technician/");
		a.set(myval);*/
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
 
for(j=0;j<sta.length;j++){
            staval=parseInt(sta[j]);

                      if(staval==1 || staval==2 || staval==3){


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