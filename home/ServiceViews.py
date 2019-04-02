from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from .views import success, fail
from .models import *
from .models import Customer, Employee, Leads, EmpStatus, Notifications, CallData, Feedbacks
from django.shortcuts import HttpResponse, render
from .tests import cleanDatabase, fill_database_with_dummy_values
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage
from home import tests
import random
import requests as req
# from django_otp.oath import hotp
import pytz
import json
import datetime
import pandas as pd
from math import cos, asin, sqrt
import pyrebase
from django.shortcuts import render
from django.contrib import auth
config = {
	'apiKey': "AIzaSyAz7fkVlG5SxgWMEmkrHC2OEaj_jcKgf4M",
    'authDomain': "aquaguard-1b328.firebaseapp.com",
    'databaseURL': "https://aquaguard-1b328.firebaseio.com",
    'projectId': "aquaguard-1b328",
    'storageBucket': "aquaguard-1b328.appspot.com",
    'messagingSenderId': "734410860053"
  };
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# This should get you all committed leads
@csrf_exempt
def approve(request):
	print("im in qc")
	values = database.child('location').get()
	data = pd.DataFrame(values.val())
	print(data.head())


#6 apis technician

#ANDROID LOGIN
@csrf_exempt
def login(request):
    if(request.method=='POST'):
        phone=request.POST.get("username",None)
        password=request.POST.get("password",None)

        if(phone==None or password==None):
            logger.debug("Invalid Login credentials pushed")
            fail("Invalid credentials")
        else:
            technician_data = Employee.objects.filter(phone=phone, password=password, type='tn')
            print(len(technician_data))
            if (len(technician_data) > 0):
                print("valid user")
                logger.debug("User Id:"+str(technician_data[0].id)+", "+technician_data[0].name+" logged in")
                out={}
                out['id']=technician_data[0].id
                return success(out)
            else:
                logger.debug("Failure in Technician Login with id"+phone)
                return fail("invalid user")

    return fail("Login is not valid")


@csrf_exempt
def checkPhone(request):
    if (request.method == "POST"):
        phone = request.POST.get('phone', None)
        print(phone)
        cust = Customer.objects.filter(mobile=phone)
        data = {}
        print("this is the legnth", len(cust))
        if (len(cust) != 0):
            data['phone'] = cust[0].mobile
            data['product_id'] = cust[0].Equipment.product_id
            data['product_name'] = cust[0].Equipment.name
            data['fname'] = cust[0].fname
            data['lname'] = cust[0].lname
            data['email'] = cust[0].email
            data['alternativeMobile'] = cust[0].alternativeMobile
            data['address'] = cust[0].address
            data['pincode'] = cust[0].pincode
            data['id'] = cust[0].id
            data['city'] = cust[0].city
            data['land'] = cust[0].land

            data['latitude'] = cust[0].latitude
            data['longitude'] = cust[0].longitude

            return success(data)
        else:
            return fail("sorry no data found")

    else:
        return fail("please do make a post request")



@csrf_exempt
def checkMail(request):
    if (request.method == "POST"):
        mail = request.POST.get('mail', None)
        print(mail)
        cust = Customer.objects.filter(email=mail)
        data = {}
        print("this is the legnth", len(cust))
        if (len(cust) != 0):
            data['phone'] = cust[0].mobile
            data['product_id'] = cust[0].Equipment.product_id
            data['product_name'] = cust[0].Equipment.name
            data['fname'] = cust[0].fname
            data['lname'] = cust[0].lname
            data['email'] = cust[0].email
            data['alternativeMobile'] = cust[0].alternativeMobile
            data['address'] = cust[0].address
            data['pincode'] = cust[0].pincode
            data['land'] = cust[0].land
            data['id'] = cust[0].id
            data['city'] = cust[0].city
            data['latitude'] = cust[0].latitude
            data['longitude'] = cust[0].longitude

            return success(data)
        else:
            return fail("sorry no data found")

    else:
        return fail("please do make a post request")


# @csrf_exempt
# def existCustomerProblemRegistration(request):
#     if (request.method == "POST"):
#         print("hello")
#         # userRelated data
#         problem_description = request.POST.get('problem', None)
#         cid = request.POST.get('cid', None)
#         print("This is problem", problem_description)
#         print(problem_description)
#         if (problem_description == None and cid == None):
#             return fail("Invalid data")
#         else:
#             customer=Customer.objects.get(id=cid)
#             current=CurrentBooking(problem_description=problem_description, customer=customer)
#             current.save()
#             return success("successfully added");
#                 # ticket_details=checkTech(customer,problem_description)
#                 # if ticket_details is not None:
#                 #     return success(ticket_details)
#                 # else:
#                 #     return fail("No technician found for your search")



#     else:
#         return fail("post operation is required")

#     print("invalid page option")
#     return HttpResponse("Invalid page")


# this is to check techinician
def checkTech(customer, problem_description):
    if (bool(customer)):
        tech = Employee.objects.filter(type="tn", pincode=customer.pincode)
        print(bool(tech))
        if (bool(tech) != False):
            tech = Employee.objects.get(type="tn", pincode=customer.pincode)

        else:
            pincode1 = customer.pincode
            pincode2 = customer.pincode
            for i in range(5):
                print(i)
                pincode1 = int(pincode1) + 1
                pincode2 = int(pincode2) - 1
                if (bool(Employee.objects.filter(type="tn", pincode=pincode1)) != False):
                    tech = Employee.objects.get(type="tn", pincode=pincode1)
                    print(pincode1)
                    break
                elif (bool(Employee.objects.filter(type="tn", pincode=pincode2)) != False):
                    tech = Employee.objects.get(type="tn", pincode=pincode2)
                    print(pincode2)
                    break
        print("it has reached here")
        ticket = CurrentBooking(problem_description=problem_description, customer=customer,technician=tech)
        ticket.save()
        ticket_details = {}
        ticket_details['ticket_id'] = ticket.bookingId
        ticket_details['resp'] = "New ticket raised"
        ticket_details['name'] = tech.name
        ticket_details['phone'] = tech.phone
        ticket_details['pin'] = tech.pincode
        return ticket_details

def deleteTicket(request):
    if(request.method=="POST"):
        id=request.POST.get("id",None)
        if(id!=None ):
            try:
                ticket=CurrentBooking.objects.get(id=id)
                ticket.delete()
                return success("Ticket deleted successfully")
            except:
                return fail("Ticket does not exist")
@csrf_exempt
def assignTechnicianToCurrentBooking(request):
    if(request.method=="POST"):
        technician_id=request.POST.get("tid",None)
        booking_id=request.POST.get("cid",None)
        if(technician_id==None or booking_id==None):
            return fail("Invalid data")
        else:
            booking=CurrentBooking.objects.get(bookingId=booking_id)
            technician=Employee.objects.get(id=technician_id)
            booking.technician=technician
            booking.save()
            return success("Booking confirmed")

                    
def displayAllAssignedTickets(request):
    booking=CurrentBooking.objects.filter(technician__isnull=False)
    out=[]
    for i in booking:
        current={}
        current['technician']=i.technician.name
        current['customer']=i.customer.fname+""+i.customer.lname
        current['problem']=i.problem_description
        current['pincode']=i.customer.pincode
        out.append(current)

    return success(out)

@csrf_exempt
def updateStatus(request):
    if (request.method=="POST"):
        id = request.POST.get("id",None)
        status = request.POST.get("status",None)
        comments = request.POST.get("comments",None)
        if(id == None ):
           return fail("No Id Found")
        else:
            lead = Customer.objects.get(id = id)
            lead.status = status
            lead.comments = comments
            # lead = Customer(status = status, comments = comments)
            lead.save()
            return success("New Lead created!")
    return HttpResponse("Error In Request")

@csrf_exempt
def empLogin(request):
    if (request.method=="POST"):
        id=request.POST.get("id",None)
        if(id == None or id==''):
            return fail("Enter Employee Id")
        else:
            try:
                employee = Employee.objects.get(id = id)

            except Employee.DoesNotExist:
                return fail("Employee Id Not Foud")
            return success('Welcome ' + employee.first_name+' ' + employee.last_name)
    return fail("Bad Request")
    
@csrf_exempt
def displaySingleLead(request):
    if (request.method=="POST"):
        id = request.POST.get("id",None)
        leadObj=Customer.objects.get(id = id)
        lead={}
        lead['fname']=leadObj.fname
        lead['lname']=leadObj.lname
        lead['email']=leadObj.email
        lead['mobile']=leadObj.mobile
        lead['alternativeMobile']=leadObj.alternativeMobile
        lead['address']=leadObj.address
        lead['land']=leadObj.land
        lead['pincode']=leadObj.pincode
        lead['status']=leadObj.status
        lead['comments']=leadObj.comments
        return success(lead)
    return HttpResponse("Error In Request")

@csrf_exempt
def displayAllLeads(request):
    if (request.method=="POST"):
        empid = request.POST.get("id",None)
        if(empid != None):
            try:
                employee = Employee.objects.get(id=empid)
            except Exception as e:
                return fail("Employee Id Not Foud")
            leads = CustomerEmployee.objects.filter(employee=employee , status='ip')
            print(leads)
            print("DATA IS OUTPUTTED OVER HERE")
            leads_list=[]
            print(len(leads))
            if(len(leads)==0):
                return fail("No employee in db")
            else:
                for i in range(len(leads)):
                    lead={}
                    lead['id']=leads[i].customer.id
                    lead['fname']=leads[i].customer.fname
                    lead['lname']=leads[i].customer.lname
                    lead['email']=leads[i].customer.email
                    lead['mobile']=leads[i].customer.mobile
                    lead['alternativeMobile']=leads[i].customer.alternativeMobile
                    lead['address']=leads[i].customer.address
                    lead['land']=leads[i].customer.land
                    lead['pincode']=leads[i].customer.pincode
                    lead['status']=leads[i].customer.status
                    lead['comments']=leads[i].customer.comments
                    leads_list.append(lead)
                return success(leads_list)
    return HttpResponse("Error In Request")


def displayCurrentBookings(request):
    try:
        booking=CurrentBooking.objects.all()
        out=[]
        for i in range(len(booking)):
            currentTicket={}
            ticket=booking[i]
            currentTicket['id']=ticket.bookingId
            currentTicket['customerName']=ticket.customer.lname+ticket.customer.fname
            currentTicket['customerPincode']=ticket.customer.pincode
            currentTicket['problem']=ticket.problem_description
            currentTicket['Customerplace']=ticket.customer.city
            if ticket.technician is None:
                currentTicket["assigned"]="false"
                out.append(currentTicket)

            else:
                currentTicket['assigned']="true"
        return success(out)
    except:
        return fail("No booking to show")

@csrf_exempt
def displayAllTickets(request):
    currentBooking = CurrentBooking.objects.all()
    ticketList = []
    for i in currentBooking:
        tick = {}
        tick['prob'] = i.problem_description
        tick['date'] = str(i.request_date)
        tick['pin'] = i.customer.pincode
        tick['phone'] = i.customer.mobile
        tick['mail'] = i.customer.email
        tick['id'] = i.bookingId
        ticketList.append(tick)
    return success(ticketList)

@csrf_exempt
def fetchDetailsFromBookingId(request):
    print(request.POST)
    if(request.method=="POST"):
        id=request.POST.get("id")
        print(id)
        data=json.loads(id)
        out=[]
        for id in data:
            # try:
            booking=CurrentBooking.objects.get(bookingId=id)

            data={}
            data['id']=booking.bookingId;
            data['technician']=booking.technician.name
            data['customer']=booking.customer.fname+" "+booking.customer.lname
            data['pincode']=booking.customer.pincode
            out.append(data)
            print(out)
            # except:
            #     print("booking not found")
        return success(out)
    else:
        return fail("invalid data")
@csrf_exempt
def displayTodaysBooking1(request):
    if(request.method=="POST"):
        out=[]
        current=CurrentBooking.objects.filter(technician__isnull=True)
        currentBook=[]
        for i in current:
            currentbook={}
            currentbook['id']=i.bookingId
            currentbook['client_name']=i.customer.fname
            currentbook['pincode']=i.customer.pincode
            currentbook['problem']=i.problem_description

            currentBook.append(currentbook)
        
        return success(currentBook)
    return fail("Request type error")


    
@csrf_exempt
def displayTodaysBooking(request):
    if(request.method=="POST"):
        technician_id=request.POST.get("technician_id",None)
        out=[]
        tech=Employee.objects.get(id=technician_id)
        current=CurrentBooking.objects.filter(technician=tech)
        currentBook=[]
        for i in current:
            currentbook={}
            currentbook['id']=i.bookingId
            currentbook['client_name']=i.customer.fname
            currentbook['area']=i.customer.address
            currentbook['pincode']=i.customer.pincode
            currentbook['phone']=i.customer.mobile
            currentbook['alternate_phone']=i.customer.alternativeMobile
            currentbook['deviceName']=i.customer.Equipment.name
            currentbook['lat']=i.customer.latitude
            currentbook['lng']=i.customer.longitude
            currentbook['deviceId']=i.customer.Equipment.product_id
            currentbook['problem']=i.problem_description

            currentBook.append(currentbook)
        
        return success(currentBook)
    return fail("Request type error")

@csrf_exempt
def displayPreviousBooking(request):
    if (request.method == "POST"):
        technician_id = request.POST.get("technician_id", None)
        out = []
        booking = {}
        out[0]['id'] = 123
        out[0]['client_name'] = "Hari Vignesh"
        out[0]['area'] = "J.p nagar 1st phase"
        out[0]['picode'] = '560078'
        out[0]['phone']="9008522228"
        out[0]['alternate_phone']="8754284170"
        out[1]={}
        out[1]['id'] = 321
        out[1]['client_name'] = "Vinnarasu"
        out[1]['area'] = "J.p nagar 2nd phase"
        out[1]['picode'] = '560077'
        out[1]['phone'] = "9008522228"
        out[1]['alternate_phone'] = "9008522227"
        return success(out)

    return fail("Request type error")

@csrf_exempt
def displayPreviousBookingAdmin(request):

    if (request.method=="POST"):
        previous=previousBooking.objects.all()

        previousBook=[]
        for i in previous:
            previousbook={}
            previousbook['id']=i.bookingId
            previousbook['client_name']=i.customer.fname
            previousbook['area']=i.customer.address
            previousbook['pincode']=i.customer.pincode
            previousbook['phone']=i.customer.mobile
            previousbook['alternate_phone']=i.customer.alternativeMobile
            previousbook['cost']=i.cost
           
            previousbook['problem']=i.problem_description

            previousBook.append(previousbook)
        return success(previousBook)
    else:
        return fail("invalid data")

@csrf_exempt
def sendUserVerficationOtp(request):
    otpurl="http://api.msg91.com/api/sendhttp.php"
    if(request.method=="POST"):
        otp=random.randint(1000,9999)
        mobile=request.POST.get("mobile",None)
        if(mobile!=None):
            params={'message':"Your ION EXCHANGE otp is "+str(otp),'authkey':'243807AWIErnmLDQ5bcc7ac9','mobiles':mobile,'sender':'MSGIND'
                    ,'country':'91','route':4}
            result=requests.get(url = otpurl, params = params)
            print(str(result.content))
            print(otp)
            return success(str(otp))
        return fail("Invalid credentials")
    return fail("invalid page")



# SHOULD ASSIGN IT TO THE EMPLOYEE OBJECT FOR THE RELATED COLOR
@csrf_exempt
def uploadServiceAudioRecording(request):
    folder = 'AudioRecording/'
    print(request.FILES)
    if request.method == 'POST' and request.FILES['myfile']:
        bookingId=request.POST.get("booking_id",None)
        myfile = request.FILES.get('myfile',None)
        if(bookingId==None or myfile==None):
            return fail("Invalid data")
        else:
            print("working")
            fs = FileSystemStorage(location=folder)  # defaults to   MEDIA_ROOT
            filename = fs.save(myfile.name, myfile)
            file_url = fs.url(filename)
            print(file_url)
            try:
                booking=CustomerEmployee.objects.get(bookingId=bookingId)
                booking.recording_data_url=file_url
                booking.save()
            except:
                return fail("Invalid booking")

        return success("File uploaded successfully")
    else:
        return success("Upload your audio over here")



@csrf_exempt
def editTechnician(request):
    if(request.method=='POST'):
        id,phone,pincode,username=request.POST.get("id",None),request.POST.get("phone",None),request.POST.get("pincode",None),request.POST.get("username",None)

        if(id==None or phone==None  or pincode==None or username==None):
            return fail("Invalid credential")
        else:
            try:
                emp=Employee.objects.get(id=id)
                emp.phone=phone
                emp.pincode=pincode
                emp.username=username
                emp.save()
                return success("Employee saved successfully")
            except:
                return fail("Invalid employee id")


@csrf_exempt
def serviceCompleted(request):
    if(request.method=="POST"):
        serviceId=request.POST.get("serviceId",None)
        cost=request.POST.get("cost",0)
        if(serviceId is not None):
            booking=CurrentBooking.objects.get(bookingId=serviceId)
            bookingLog=previousBooking(bookingId=booking.bookingId,customer=booking.customer,technician=booking.technician
                                       ,problem_description=booking.problem_description,request_date=booking.request_date
                                        ,recording_data_url=booking.recording_data_url)
            bookingLog.cost=cost
            bookingLog.save()
            return success("booking completed successfully")
        else:
            return fail("booking could not be completed")


@csrf_exempt
def updateCustomerLocation(request):
    if(request.method=="POST"):
        bookingId=request.POST.get("bookingId",None)
        lat=request.POST.get("lat",0)
        lng=request.POST.get("lng",0)
        if((bookingId is not None) and not(lat==0) and not(lng==0)):
            try:
                booking=CurrentBooking.objects.get(bookingId=bookingId)
                customer=booking.customer
                customer.latitude=lat
                customer.longitude=lng
                customer.save()
                return success("New User Location saved")
            except:
                return fail("error while trying to save location")
        else:
            fail("error")


@csrf_exempt
def fetchTechnicianToCustomerDistances(request):
    if(request.method=="POST"):
        bookingId=request.POST.get("bookingId",None)
        data=request.POST.get("data",None)

        data=json.loads(data)
        print(data)
        out={}

        for i in data:
            print("loop")
            print(i)
            result = requests.get(url=i['url'],verify=False)
            # print("this is the result")
            # print(str(result.json))
            # print("this is jsons")
            # jsondata=result.json()
            #
            # print(jsondata)
            # print(jsondata['routes'][0]['legs'][0]['time'])
            # out[i['bookingId']]=jsondata['routes'][0]['legs'][0]['time']
            sa=result.content
            decoded=sa.decode('utf-8')
            abc=json.loads(decoded)
            out[i['bookingId']] = []
            out[i['bookingId']].append(abc['routes'][0]['legs'][0]['duration']['text'])
            out[i['bookingId']].append(abc['routes'][0]['legs'][0]['distance']['text'])

        

            # print(json.loads(decoded))
            #print(result)
        return success(out)

    return fail("Some error")

