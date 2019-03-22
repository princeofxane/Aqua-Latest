from django.shortcuts import render,HttpResponse
from .models import Employee, Customers, Product, Complaints
# from .models import Employee,Customer,CurrentBooking,Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from .views import fail, success

# register a complaint
@csrf_exempt
def createComplaint(request):
    if(request.method=="POST"):
        technician_id = request.POST.get('tech_id', None)
        cust_id = request.POST.get('cust_id', None)
        location = request.POST.get('location', None)
        address = request.POST.get('address', None)
        pincode = request.POST.get('pincode', None)
        appointmentTime = request.POST.get('appointmentTime', None)
        subject = request.POST.get('subject', None)
        problem_description = request.POST.get('problem_description', None)
        recording_data_url = request.POST.get('recording_url', None)
        severity = request.POST.get('severity', None)

        try:
            custObj = Customers.objects.get(custID=cust_id)
        except Exception as e:
            return fail("Customer doesn't exist")

        try:
            technicianObj = Employee.objects.get(empID=technician_id)
        except Exception as e:
            return fail("Employee doesn't exist")
        

        complaint = Complaints()
        complaint.bookingID = generateRandomID()
        complaint.technicianID = technicianObj
        complaint.customer = custObj
        complaint.location = location
        complaint.address = address
        complaint.pincode = pincode
        complaint.appointmentTime = appointmentTime
        complaint.subject = subject
        complaint.problem_description = problem_description
        complaint.recording_data_url = recording_data_url
        complaint.severity = severity
        complaint.isActive = True
        complaint.save()
        return success("Complaint has been saved")
    return fail("Error in request")





# register a complaint
@csrf_exempt
def updateComplaint(request):
    timeNow = str(datetime.datetime.now())
    if(request.method=="POST"):
        bookingID = request.POST.get('bookingID', None)
        technician_id = request.POST.get('tech_id', None)
        cust_id = request.POST.get('cust_id', None)
        location = request.POST.get('location', None)
        address = request.POST.get('address', None)
        pincode = request.POST.get('pincode', None)
        appointmentTime = request.POST.get('appointmentTime', None)
        subject = request.POST.get('subject', None)
        problem_description = request.POST.get('problem_description', None)
        recording_data_url = request.POST.get('recording_url', None)
        severity = request.POST.get('severity', None)
        isActive = request.POST.get('isActive', None)

        try:
            complaintObj = Complaints.objects.get(bookingID=bookingID)
        except Exception as e:
            return fail("Complaint doesn't exist to update")

        try:
            technicianObj = Employee.objects.get(empID=technician_id)
        except Exception as e:
            return fail("Technician doesn't exist to update")


        complaintObj.location = location
        complaintObj.address = address
        complaintObj.pincode = pincode
        complaintObj.appointmentTime = pincode
        complaintObj.severity = severity
        complaintObj.subject = subject
        complaintObj.technician = technicianObj
        complaintObj.recording_data_url = recording_data_url
        oldDescription = complaintObj.problem_description
        newDescription = oldDescription + "\n\n\n" + "----------------------------" + "\n" + problem_description + "\n" + "----------------------------" + "\n" + timeNow + ' ' + technician_id
        complaintObj.save()
        return success("Complaint has been saved")
    return fail("Error in request")


# Fn to get all complains registered by given customer.
@csrf_exempt
def getAllComplaints(request):
    if request.method == "POST":
        cust_id = request.POST.get('cust_id', None)

        try:
            custObj = Customers.objects.get(id=cust_id)
            complaintObj = Complaints.objects.filter(customerID=custObj, isActive=True)
        except Exception as e:
            return fail("There is no complaint existing by this customer")

        complaint_list = []
        for eachComplaint in complaintObj:
            complaint = {}
            complaint["createdDate"] = eachComplaint.createdDate
            complaint["location"] = eachComplaint.location
            complaint["address"] = eachComplaint.address
            complaint["pincode"] = eachComplaint.pincode
            complaint["appointmentTime"] = eachComplaint.appointmentTime
            complaint["subject"] = eachComplaint.subject
            complaint["problem_description"] = eachComplaint.problem_description
            complaint["request_date"] = eachComplaint.request_date
            complaint["recording_date_url"] = eachComplaint.recording_data_url
            complaint["severity"] = eachComplaint.severity
            complaint_list.append(complaint)
        return success(complaint_list)
    return fail("Error in request")
            



# def displayAllTickets(request):
#     currentBooking=CurrentBooking.objects.all()
#     for i in range(len(currentBooking)):
#         ticket={}

@csrf_exempt
def checkPhone(request):
    if (request.method=="POST"):
        phone=request.POST.get('phone',None)
        print(phone)
        cust=Customers.objects.filter(mobile=phone)
        data={}
        print("this is the legnth",len(cust))
        if(len(cust) != 0):
            data['phone']=cust[0].mobile
            data['product_id']=cust[0].Equipment.product_id
            data['product_name']=cust[0].Equipment.name
            data['fname']=cust[0].fname
            data['lname']=cust[0].lname
            data['email']=cust[0].email
            data['alternativeMobile']=cust[0].alternativeMobile
            data['address']=cust[0].address
            data['pincode']=cust[0].pincode
            data['id']=cust[0].id

            return success(data)
        else:
            return fail("sorry no data found")

    else:
        return fail("please do make a post request")

@csrf_exempt
def checkMail(request):
    if (request.method=="POST"):
        mail=request.POST.get('mail',None)
        print(mail)
        cust=Customers.objects.filter(email=mail)
        data={}
        print("this is the legnth",len(cust))
        if(len(cust) != 0):
            data['phone']=cust[0].mobile
            data['product_id']=cust[0].Equipment.product_id
            data['product_name']=cust[0].Equipment.name
            data['fname']=cust[0].fname
            data['lname']=cust[0].lname
            data['email']=cust[0].email
            data['alternativeMobile']=cust[0].alternativeMobile
            data['address']=cust[0].address
            data['pincode']=cust[0].pincode
            data['land']=cust[0].land
            data['id']=cust[0].id

            return success(data)
        else:
            return fail("sorry no data found")

    else:
        return fail("please do make a post request")

# @csrf_exempt
# def existCustomerProblemRegistration(request):
#     if(request.method=="POST"):
#         print("hello")
#         #userRelated data
#         problem_description=request.POST.get('problem',None)
#         cid=request.POST.get('cid',None)
#         print("This is problem",problem_description)
#         print(problem_description)
#         if(problem_description==None and cid==None ):
#             return fail("Invalid data")
#         else:
#             # device problem registration
           
#             customer=Customer.objects.get(id=cid)

#             if (customer.id >= 0):
#                 ticket = CurrentBooking(problem_description=problem_description, customer=customer)
#                 ticket.save()
#                 ticket_details = {}
#                 ticket_details['ticket_id'] = ticket.bookingId
#                 ticket_details['resp'] = "New ticket raised"
#                 return success("ticke is hosted")
#     else:
#         return fail("post operation is required")

#     print("invalid page option")
#     return HttpResponse("Invalid page")


def generateRandomID():
    randomID = 'TC' + '{0:06}'.format(random.randint(1, 100000))
    return randomID
