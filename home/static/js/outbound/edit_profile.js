function readURL(input)
{
    if (input.files && input.files[0])
    {
        var reader = new FileReader();
        reader.onload = function (e) 
        {
            $('#blah').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

var emp_id;

$(document).ready(function ()
{
    /*$.post(baseUrl + "getSession/", {},
        function (data, status) {
            dataObj = JSON.parse(data);
            if (dataObj.result == "fail") {
                window.location.href = baseUrl
            } else {
                emp_id = dataObj.description;
                // getUserData(emp_id);
                console.log(emp_id);
            }
        });
*/
emp_id = 1002;
    $("#cancelButton").click(function () 
        {
            $.ajax({
                type: "POST",
                url:"/outbound/home",
                success: function(data)
                {}
            });
            //window.location.href = baseUrl + "homePage/"
        });

    $("#doneButton").click(function () {
        var fd = new FormData();
        var files = $('#profilepic')[0].files[0];
        fd.append('id', emp_id);
        fd.append('profile_logo', files);

        $.ajax({
            url: "/outbound/edit_profile",
            type: 'POST',
            data: fd,
            contentType: false,
            processData: false,
            success: function (response, data, description)
            {
                dataObj=JSON.parse(response);
                if(dataObj.result=="fail") 
                {
                    //alert(dataObj.description);
                    alert("Image Upload Failed.");
                }
                else
                {
                    //alert(dataObj.description);
                    alert("Profile Changed Sucessfully.");
                    $.ajax({
                        type: "POST",
                        url:"/outbound/home",
                        success: function(data)
                        {}
                    });
                }
            },
        });
    });

});
