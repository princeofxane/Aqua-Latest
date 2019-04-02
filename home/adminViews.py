from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from .views import success, fail
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
# import gmaps

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


@csrf_exempt
def ib_homePage(request):
    return render(request,"ib_index.html")



@csrf_exempt
def teamlead(request):
    return render(request,"teamlead.html")


@csrf_exempt
def techadd(request):
    return render(request,"add_technician.html")

@csrf_exempt
def prodview(request):
    return render(request,"product_view.html")



@csrf_exempt
def currWork(request):
    return render(request,"booking.html")


@csrf_exempt
def inventory(request):
    return render(request,"inventory.html")

@csrf_exempt
def viewingbooking(request):
    return render(request, 'view_booking.html')

@csrf_exempt
def previousbook(request):
    return render(request, 'previous_booking.html')

@csrf_exempt
def currentbookview(request):
    return render(request, 'current_booking.html')

@csrf_exempt
def tickview(request):
    return render(request, 'ticket_view.html')


@csrf_exempt
def techview(request):
    return render(request, 'technician_view.html')


@csrf_exempt
def addtick(request):
    return render(request, 'add_ticket.html')

# @csrf_exempt
# def addtick(request):
#     return render(request, 'create_ticket.html')

@csrf_exempt
def addprod(request):
    return render(request, 'add_products.html')

#----------------------- Page Renders ---------------------------#
@csrf_exempt
def loginPage(request):
    return render(request, 'loginPage.html')

@csrf_exempt
def Test(request):
    return render(request, 'base.html')

@csrf_exempt
def remarks(request):
    return render(request, 'remarks.html')


@csrf_exempt
def setEmpTargetPage(request):
    return render(request, 'set_employee_target.html')

@csrf_exempt
def reportsPage(request):
    print("im coming here")
    return render(request, 'reports.html')

@csrf_exempt
def tc_homePage(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'index.html')

@csrf_exempt
def ob_qc_homePage(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'ob_qc.html')

@csrf_exempt
def tc_dashboard(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'tc_dashboard.html')

@csrf_exempt
def obAdmin_tc_homePage(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'obAdmin_tc_homePage.html')

@csrf_exempt
def obAdmin_callHistoryPage(request):
    return render(request, 'obAdmin_callHistoryPage.html')

@csrf_exempt
def obAdmin_commitHistoryPage(request):
    return render(request, 'obAdmin_commitHistoryPage.html')

@csrf_exempt
def obAdmin_reportsPage(request):
    print("im coming here")
    return render(request, 'obAdmin_reportsPage.html')

@csrf_exempt
def inboundHome(request):
    print()
    return render(request,"inbound.html")


@csrf_exempt
def ad_homePage(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        loginPage(request)
    return render(request, 'admin_employee.html')


@csrf_exempt
def homePageCommittedLeads(request):
    return render(request, 'committedLeads.html')


@csrf_exempt
def Edit_Remarks(request):
    return render(request, 'remarks.html')


@csrf_exempt
def homePageContactLeads(request):
    return render(request, 'contactLeads.html')

@csrf_exempt
def callHistoryPage(request):
    return render(request, 'call_history.html')

@csrf_exempt
def mainEmployee(request):
    return render(request, 'employee.html')

@csrf_exempt
def addEmployee(request):
    return render(request, 'employee.html')


@csrf_exempt
def admin_tasks(request):
    return render(request, 'admin_tasks.html')


@csrf_exempt
def assign_employee(request):
    return render(request, 'assign_employee.html')


@csrf_exempt
def leads_delete(request):
    return render(request, 'leads_delete.html')


@csrf_exempt
def commitHistoryPage(request):
    return render(request, 'commits_board.html')

@csrf_exempt
def forgotPassword(request):
    return render(request, 'forgotpassword.html')

@csrf_exempt
def adminStatistics(request):
    return render(request,'admin_dashboard.html')


@csrf_exempt
def adminTask(request):
    return render(request,'admin_tasks.html')


@csrf_exempt
def assign_Employee(request):
    return render(request,'assign_employee.html')

@csrf_exempt
def Add_Leads(request):
    return render(request,'add_leads.html')

@csrf_exempt
def Reassign_Leads(request):
    return render(request,'reassign_leads.html')

@csrf_exempt
def Lead_Status(request):
    return render(request,'Lead_Status.html')

@csrf_exempt
def Assign_Leads(request):
    return render(request,'assign_employee.html')


@csrf_exempt
def logoutPage(request):
    return render(request, 'logoutPage.html')


@csrf_exempt
def changedp_tc(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        #condition to check what home page to redirect
        tc_homePage(request)
    return render(request, 'change_dp_tc.html')


@csrf_exempt
def changedp_ad(request):
    currentSession = getSession(request, True)
    if currentSession == '':
        #condition to check what home page to redirect
        tc_homePage(request)
    return render(request, 'change_dp_tc.html')
#----------------------- Api's ---------------------------#


@csrf_exempt
def storeSession(request):
    id = request.POST.get("id", None)
    if(id == None or id == ''):
        return fail("Haven't received any emp_id to create session")
    else:
        try:
            request.session['emp_id'] = id
        except Exception as e:
            return fail("Employee Id Not Foud")
        
        return success("Session stored")


@csrf_exempt
def getSession(request, isLocalUse=None):
    if (request.method == "POST"):
        if isLocalUse:
            if 'emp_id' in request.session:
                sessionID = request.session['emp_id']
                return sessionID
            return ''
        else:
            if 'emp_id' in request.session:
                sessionID = request.session['emp_id']
                if (sessionID == ''):
                    return fail("You need to login")
                return success(sessionID)
            return fail("You need to login")
    return fail("Bad request")


@csrf_exempt
def flushSession(request, isLocalUse=None):
    if (request.method == "POST"):
        request.session.flush()
        return success("Session cleared")


# @csrf_exempt
# def generateOTP(request):
#     if (request.method == "POST"):
#         secret_key = b'1234567890123467890'
#         now = int(time.time())
#         for delta in range(10, 110, 20):
#             print(totp(key=secret_key, step=10, digits=6, t0=(now-delta)))

@csrf_exempt
def getUserData(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Enter Employee Id")
        try:
            # get his first and lastname
            employee = Employee.objects.get(empID=id)
        except Exception as e:
            return fail("Employee Id Not Foud")

        empStatus = getEmpLogInfo(employee)
        if empStatus != None:
            loginTime = empStatus.loginTime
        else:
            loginTime = None

        dataReturn = {
            "fname": employee.fname,
            "lname": employee.lname,
            "loginTime": loginTime
        }
        return success(dataReturn)


    return fail("Invalid method")


@csrf_exempt
def addProfilePicture(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Provide employee id")
        else:
            try:
                employee = Employee.objects.get(empID = id)
            except Exception as e:
                return fail("Employee Id Not Foud")
            employee.profile_logo = request.FILES['profile_logo']
            file_type = employee.profile_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return fail("Image file must be PNG, JPG, or JPEG")
            employee.save()            
        return success("Picture Uploaded Successfully")
    return fail("Bad request")


@csrf_exempt
def getProfilePicture(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Provide employee id")
        else:
            try:
                empObj = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Foud")
            try:
                imageUrl =  empObj.profile_logo.url
            except Exception as e:
                imageUrl = ''
            return success(imageUrl)
    return fail("Bad request")


@csrf_exempt
def setNotification(request):
    if (request.method == "POST"):
        noteForAll = False
        noteType = request.POST.get("noteType", None)
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time())
        time = time[:8]
        id = request.POST.get("id", None)
        message = request.POST.get("message", None)
        if message == None or message == '':
            return fail("Message Cannot Be NULL")
        if id == None or id == '':
            noteForAll = True
            employee = None
        else:
            try:
                employee = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Found")
        note = Notifications(message=message, date=date, employeeID=employee,
                             time=time, noteType=noteType, noteForAll=noteForAll)
        note.save()
        return success("Notification Successfully Triggered")
    return fail("Bad request")


@csrf_exempt
def getNotification(request):
    if (request.method == "POST"):
        noteForAll = False
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time())
        time = time[:8]
        message = None
        id = request.POST.get("id", None)
        # noteType = request.POST.get("noteType", None)
        if id == None or id == '':
            employee = None
            noteForAll = True
        else:
            try:
                employee = Employee.objects.get(empID=id)
            except Exception as e:
                return fail("Employee Id Not Found")
        notes = Notifications.objects.all().filter(
            employeeID=employee, noteType=noteType, date=date, noteForAll=noteForAll)
        if len(notes) == 0:
            return fail("No Noification Today")
        else:
            notes_list = []
            for note in notes:
                eachRow = {}
                eachRow['message'] = note.message
                eachRow['time'] = note.time
                notes_list.append(eachRow)
            return success(notes_list)
    return fail("Bad request")


@csrf_exempt
def togglePause(request):
    if (request.method == "POST"):
        timeNow = str(datetime.datetime.now())
        currDate = str(datetime.datetime.now().date())

        emp_id = request.POST.get("id", None)
        isPause = request.POST.get("isPause", None)
        if emp_id == None or emp_id == '':
            return fail("Enter Employee Id")
        try:
            empObj = Employee.objects.get(empID=emp_id)
            empStatObj = EmpStatus.objects.get(employeeID=empObj, date=currDate)
        except Exception as e:
            print(e)
            return fail("Couldn't get desired object")
        else:
            if isPause == 'true':
                empStatObj.pauseTime = timeNow
                empStatObj.isPause = True
                empStatObj.save()
                return success("Pause time has been captured")
            if isPause == 'false':
                duration = calculatePauseDuration(empStatObj.pauseTime)
                empStatObj.pauseTime = ''
                empStatObj.isPause = False
                empStatObj.save()
                return success(duration)
    return fail("Error in request")

def calculatePauseDuration(pauseTime):
    timeNow = datetime.datetime.now()
    pTime = datetime.datetime.strptime(pauseTime, "%Y-%m-%d %H:%M:%S.%f")
    deltaObj = datetime.timedelta(hours=pTime.hour, minutes=pTime.minute, seconds=pTime.second)
    pauseDuration = timeNow - deltaObj
    return str(pauseDuration)

@csrf_exempt
def storeEmpLog(emp, isLoggingIn):
    timeNow = datetime.datetime.now()
    dateToString = str(datetime.datetime.now().date())
    try:
        # The try would pass if it isn't a new employee, else there wont be an entry with date column
        empStatus = EmpStatus.objects.get(employeeID = emp, date = str(datetime.datetime.now().date()))
    except Exception as e:
        # This is for a new employee.
        empStatus = EmpStatus()
        empStatus.employeeID = emp
        empStatus.loginTime = timeNow
        empStatus.date = dateToString
        empStatus.save()

        #employee made active
        emp.isActive = True
        emp.save()
    finally:
        if isLoggingIn is True:

            # If it is a new day the login timstamp need to be stored
            if empStatus.date != str(datetime.datetime.now().date()):
                empStatus.employeeID = emp
                empStatus.loginTime = timeNow
                empStatus.date = dateToString
                empStatus.save()

                #employee made active
                emp.isActive = True
                emp.save()
        else:
            empStatus.logoutTime = timeNow
            empStatus.save()

            #employee made inactive
            emp.isActive = False
            emp.save()

            # print("This is the time now")
            # print(timeNow.time().replace(second=0, microsecond=0))
            # print(timeNow.date())


@csrf_exempt
def getEmpLogInfo(empInstance):
    try:
        currDate = str(datetime.datetime.now().date())
        
        # Taking only initial login time. there can be multiple logins.
        empStatus = EmpStatus.objects.get(employeeID = empInstance, date = currDate)
       
        if empStatus == None:
            return None
        return empStatus
    except Exception as e:
        print(e)


@csrf_exempt
def empLoginCheck(request):
    if (request.method == "POST"):
        # tests.addEmployees()
        # tests.addDummyLeads()
        id = request.POST.get("id", None)
        password = request.POST.get("password", None)
        if id == None or id == '':
            return fail("Enter Employee Id")
        else:
            try:
                employee = Employee.objects.get(empID = id)

            except Exception as e:
                return fail("Employee Id Not Foud")

            #password check
            if password != employee.password:
                return fail("Wrong password")
                
            #handle session here
            # storeSession(request)

            #store employee login information here.
            storeEmpLog(employee, True)

            return success(employee.role)
    return fail("Error in Request")


@csrf_exempt
def storeLogoutTime(request):
    if (request.method == "POST"):
        id = request.POST.get("id", None)
        if id == None or id == '':
            return fail("Provide employee id")
        else:
            timeNow = str(datetime.datetime.now())
            dateToday = str(datetime.datetime.now().date())
            employee = Employee.objects.get(empID = id)
            empStatus = EmpStatus.objects.get(employeeID = employee, date = dateToday)
            empStatus.logoutTime = timeNow
            empStatus.save()

            #Make employee inactive
            storeEmpLog(employee, False)
        return success("logoutTime has been saved")
    return fail("Bad request")


# If you want to manually add a lead
@csrf_exempt
def addNewLead(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        mobile = request.POST.get("mobile", None)
        email = request.POST.get("email", None)
        address = request.POST.get("address", None)
        pincode = request.POST.get("pincode", None)
        alternatePhone = request.POST.get("alternatePhone", None)
        purchaseDate = request.POST.get("purchaseDate", None)
        if(fname == None or lname ==  None or mobile ==  None or email ==  None or
                address ==  None or pincode ==  None or purchaseDate == None or alternatePhone ==  None):
           return fail("Invalid details")
        lead = Leads(leadID = generateRandomLeadID(), fname = fname, lname = lname, mobile = mobile, email = email,
            address = address, pincode = pincode, purchaseDate = purchaseDate, alternatePhone = alternatePhone)
        lead.save()
        return success("New Lead created!")
    return fail("Invalid Admin Page")

@csrf_exempt
def deleteSingleLead(request):
    if request.method == "POST":
        LeadID = request.POST.get("lead_id", None)
        if LeadID == None or LeadID == "":
            return fail("Id hasn't been provided")
        try:
            leadObj = Leads.objects.get(leadID = LeadID)
        except Exception as e:
            return fail("Lead not found")
        leadObj.delete()       
        return success("The lead has been deleted")
    return fail("Error in request")

@csrf_exempt
def deleteMultipleLeads(request):
    if request.method == "POST":
        LeadIDs = request.POST.getlist("leadIDs[]", None)
        if len(LeadIDs) == 0:
            return fail("No leads have selected")
        # for leadID in LeadIDs:
        try:
            leadObj = Leads.objects.filter(leadID__in=(LeadIDs)).delete()
        except Exception as e:
            return fail("Something went wrong")
        return success("Leads have successfully deleted")
    return fail("Error in request")


# This should get you all leads that you have given to deal with
@csrf_exempt
def getAssignedLeads(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)
        if emp_id != None:
            try:
                empObj = Employee.objects.get(empID=emp_id)
            except Exception as e:
                return fail("Employee Id Not Foud")
            try:
                leads = Leads.objects.filter(assignee=empObj, isInterested=False, isContacted=False)
                print(leads)
            except Exception as e:
                print(e)

            if len(leads) == 0:
                return fail("No leads in db")
            else:
                leads_list = []
                for lead in leads:
                    eachRow = {}
            #     for i in range(len(leads))
            #         lead={}
                    eachRow['leadID'] = lead.leadID
                    eachRow['fname'] = lead.fname
                    eachRow['lname'] = lead.lname
                    eachRow['email'] = lead.email
                    eachRow['phone'] = lead.phone
                    eachRow['address'] = lead.address
                    eachRow['createdDate'] = str(lead.createdDate)
                    eachRow['pincode'] = lead.pincode

                    #handle feedback
                    try:
                        feedbacksObj = Feedbacks.objects.filter(leadID=lead)
                    except Exception as e:
                        eachRow['feedback'] = ''
                    else:
                        if len(feedbacksObj) != 0:
                            feedBackArray = []
                            for feedbackObj in feedbacksObj:
                                feedBackArray.append(feedbackObj.feedback)
                            eachRow['feedback'] = feedBackArray
                        else:
                            eachRow['feedback'] = ''

                    eachRow['appointmentDate'] = lead.appointmentDate
                    eachRow['isInterested'] = lead.isInterested
                    leads_list.append(eachRow)
                return success(leads_list)
        return fail("Provide id")
    return fail("Error In Request")



# This should get you all leads that you have given to deal with
@csrf_exempt
def getComittedLeads(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)
        if emp_id != None:
            try:
                empObj = Employee.objects.get(empID=emp_id)
            except Exception as e:
                print("******************")
                return fail("Employee Id Not Foud")
            try:
                leads = Leads.objects.filter(isInterested=True)

            except Exception as e:
                print(e)
            if len(leads) == 0:
                return fail("No leads in db")
            else:
                leads_list = []
                for lead in leads:
                    eachRow = {}
            #     for i in range(len(leads))
            #         lead={}
                    eachRow['leadID'] = lead.leadID
                    eachRow['fname'] = lead.fname
                    eachRow['lname'] = lead.lname
                    eachRow['email'] = lead.email
                    eachRow['phone'] = lead.phone
                    eachRow['address'] = lead.address
                    eachRow['appointmentDate'] = str(lead.appointmentDate)
                    eachRow['comments'] = lead.comments

                    #handle feedback
                    try:
                        feedbacksObj = Feedbacks.objects.filter(leadID=lead)
                    except Exception as e:
                        eachRow['feedback'] = ''
                    else:
                        if len(feedbacksObj) != 0:
                            feedBackArray = []
                            for feedbackObj in feedbacksObj:
                                feedBackArray.append(feedbackObj.feedback)
                            eachRow['feedback'] = feedBackArray
                        else:
                            eachRow['feedback'] = ''

                    eachRow['appointmentDate'] = lead.appointmentDate
                    eachRow['isInterested'] = lead.isInterested
                    leads_list.append(eachRow)
                return success(leads_list)
        return fail("Provide id")
    return fail("Error In Request")


@csrf_exempt
def getAllUnAssignedLeads(request):
    if request.method == "POST":
        leadsObj = Leads.objects.filter(assignee = None)
        if len(leadsObj) == 0:
            return fail("No un-assigned leads available")
        leads_list = []
        for leadObj in leadsObj:
            eachRow = {}
            eachRow['leadID'] = leadObj.leadID
            eachRow['fname'] = leadObj.fname
            eachRow['lname'] = leadObj.lname
            eachRow['address'] = leadObj.address
            eachRow['createdDate'] = str(leadObj.createdDate)
            eachRow['email'] = leadObj.email
            eachRow['phone'] = leadObj.phone
            eachRow['alternatePhone'] = leadObj.alternatePhone
            eachRow['purchaseDate'] = leadObj.purchaseDate
            eachRow['pincode'] = leadObj.pincode
            leads_list.append(eachRow)
        return success(leads_list)
    return fail("Error in request")


# This should get you all committed leads
@csrf_exempt
def getInterestedLeads(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id', None)
        # leads = Leads.objects.all().filter(isInterested=True)
        try:
            empObj = Employee.objects.get(empID=emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")

        try:
            leadsObj = Leads.objects.filter(isInterested=True,assignee=empObj)
        except Exception as e:
            return fail("Something went wrong")

        if len(leadsObj) == 0:
            print("************************")
            return fail("No committed leads")
        else:
            leads_list = []
            for lead in leadsObj:
                print(lead.assignee)
                eachRow = {}
        #     for i in range(len(leads))
        #         lead={}
        #         lead['id']=leads[i].customer.id
                eachRow['leadID'] = lead.leadID
                eachRow['fname'] = lead.fname
                eachRow['lname'] = lead.lname
                eachRow['email'] = lead.email
                eachRow['phone'] = lead.phone
                eachRow['address'] = lead.address
                eachRow['appointmentDate'] = str(lead.appointmentDate)
                eachRow['comments'] = lead.comments
                leads_list.append(eachRow)
            return success(leads_list)
    return fail("Error In Request")


@csrf_exempt
def getCallbackLeads(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)

        try:
            empObj = Employee.objects.get(empID=emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")
        try:
            leadObj = Leads.objects.filter(callAction='cb', assignee=empObj)
        except Exception as e:
            print("Something went wrong")
        leads_list = []
        for lead in leadObj:
            eachRow = {}
            print("im coming")
    #     for i in range(len(leads))
    #         lead={}
    #         lead['id']=leads[i].customer.id
            eachRow['leadID'] = lead.leadID
            eachRow['fname'] = lead.fname
            eachRow['lname'] = lead.lname
            eachRow['email'] = lead.email
            eachRow['phone'] = lead.phone
            eachRow['address'] = lead.address
            eachRow['appointmentDate'] = str(lead.appointmentDate)
            eachRow['comments'] = lead.comments
            leads_list.append(eachRow)
        return success(leads_list)
    return fail("Error In Request")


@csrf_exempt
def setCommit(request):
    if request.method == "POST":
        lead_id = request.POST.get("lead_id", None)
        if lead_id == None or lead_id == '':
            return fail("Lead id has not provided")
        try:
            leadObj = Leads.objects.get(leadID=lead_id)
        except Exception as e:
            return fail("Lead doesn't exist")
        isCommit = request.POST.get("isCommit", None)
        if isCommit:
            leadObj.isInterested = True
            leadObj.save()
            return success("Lead stored as committed")
        else: 
            leadObj.isInterested = False
            leadObj.save()
            return success("Lead stored as Not Committed")
    return fail("Error in request")


# This should get you all leads yet to be called
@csrf_exempt
def getLeadsNotContacted(request):
    if request.method == "POST":
        emp_id = request.POST.get("id", None)
        if emp_id == None or emp_id == "":
            return fail("EmpID required")
        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")

        leads = Leads.objects.filter(assignee=empObj, isContacted = False)
        if len(leads) == 0:
            return fail("No employee in db")
        else:
            leads_list = []
            for lead in leads:
                eachRow = {}
        #     for i in range(len(leads))
        #         lead={}
        #         lead['id']=leads[i].customer.id
                eachRow['leadID'] = lead.leadID
                eachRow['fname'] = lead.fname
                eachRow['lname'] = lead.lname
                eachRow['email'] = lead.email
                eachRow['phone'] = lead.phone
                eachRow['address'] = lead.address
                eachRow['createdDate'] = str(lead.createdDate)
                eachRow['pincode'] = lead.pincode
                eachRow['source'] = lead.source
                leads_list.append(eachRow)
            return success(leads_list)
    return fail("Error In Request")

@csrf_exempt
def getContactedLeads(request):
    if request.method == "POST":
        leads = Leads.objects.all().filter(isContacted=True)
        if len(leads) == 0:
            return fail("No employee in db")
        else:
            leads_list = []
            for lead in leads:
                eachRow = {}
        #     for i in range(len(leads))
        #         lead={}
        #         lead['id']=leads[i].customer.id
                eachRow['leadID'] = lead.leadID
                eachRow['fname'] = lead.fname
                eachRow['lname'] = lead.lname
                eachRow['email'] = lead.email
                eachRow['phone'] = lead.phone
                eachRow['address'] = lead.address
                eachRow['createdDate'] = str(lead.createdDate)
                eachRow['pincode'] = lead.pincode   
                leads_list.append(eachRow)
            return success(leads_list)
    return fail("Error In Request")

#update lead function
@csrf_exempt
def editLead(request):
    if request.method == "POST":
        timeNow = str(datetime.datetime.now())
        # Also require employee id to store along with remarks
        # emp_id = request.POST.get("emp_id", None)

        emp_id = request.POST.get("emp_id", None)
        leadID = request.POST.get("leadID", None)
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        address = request.POST.get("address", None)
        email = request.POST.get("email", None)
        alternatePhone = request.POST.get("alternatePhone", None)
        purchaseDate = request.POST.get("purchaseDate", None)
        product = request.POST.get("product", None)
        pincode = request.POST.get("pincode", None)
        comment = request.POST.get("comments", None)
        callAction = request.POST.get("callAction", None)
        isInterested = request.POST.get("isCommit", None)
        pincode = request.POST.get("pincode",None)
        assignee = request.POST.get("assignee",None)
        appointmentDate = request.POST.get("appointmentDate", None)

        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            print("Employee doesn't exist")
        
        try:
            leadObj = Leads.objects.get(leadID=leadID)
        except Exception as e:
            print(e)
            return fail("Lead is not present in the db")

        if fname is not '':
            leadObj.fname = fname
        if lname is not '':
            leadObj.lname = lname
        if address is not '':
            leadObj.address = address
        if email is not '':
            leadObj.email = email
        if product is not '':
            leadObj.product = product
        if alternatePhone is not '':
            leadObj.alternatePhone = alternatePhone
        if purchaseDate is not '':
            leadObj.purchaseDate = purchaseDate
        if product is not '':
            leadObj.product = product
        if pincode is not '':
            leadObj.pincode = pincode
        if appointmentDate is not '':
            leadObj.appointmentDate = appointmentDate
        if comment is not '':
            feedbackObj = Feedbacks(empID=empObj, leadID=leadObj, feedback=comment)
            feedbackObj.save()

            # oldComment = str(lead.comments)
            # newComment = oldComment + "\n\n\n" + "----------------------------" + "\n" + comment + "\n" + "----------------------------" + "\n" + str(timeNow) + ' ' + emp_id
            # newComment = oldComment + "*" + comment + "\n" + "----------------------------" + "\n" + str(timeNow) + ' ' + emp_id
            # lead.comments = newComment
        leadObj.callAction = callAction

        if isInterested == 'true':
            leadObj.isInterested = True
        if isInterested == 'false':
            leadObj.isInterested = False
        leadObj.save()
        return success("Lead info updated")
    return fail("Error in request")


@csrf_exempt
def getSingleLead(request):
    if (request.method == "POST"):
        leadID = request.POST.get("leadID", None)
        try:
            leadObj = Leads.objects.get(leadID=leadID)
        except expression as identifier:
            return fail("Lead Not Found")
        lead = {}

        lead['leadID'] = leadObj.leadID
        lead['fname'] = leadObj.fname
        lead['lname'] = leadObj.lname
        lead['email'] = leadObj.email
        lead['product'] = leadObj.product
        lead['phone'] = leadObj.phone
        lead['alternatePhone'] = leadObj.alternatePhone
        lead['address'] = leadObj.address
        lead['callAction'] = leadObj.callAction
        lead['createdDate'] = str(leadObj.createdDate)
        lead['appointmentDate'] = leadObj.appointmentDate
        lead['purchaseDate'] = leadObj.purchaseDate
        lead['pincode'] = leadObj.pincode
        #----------------------------------------

        # addr = leadObj.address.replace(" ", "+")
        # api_key = 'AIzaSyCKrObWSq1_SI_Abkr71Rdo3pKx29KJGJM'
        # uri = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=' + api_key
        # response = req.get(uri)
        # resp_json_payload = response.json()
        # customerLocation = (resp_json_payload['results'][0]['geometry']['location'])

        # example = {'lat': 13.0289365, 'lng': 77.63892249999999}

        #Example agent position list
        # technicianCordinates = [{'test': 'prince', 'lat': 39.7612992, 'lng': -86.1519681}, 
        #         {'test': 'sony', 'lat': 39.762241, 'lng': -86.158436 }, 
        #         {'test': 'amma', 'lat': 39.7622292, 'lng': -86.1578917}]

        # print(closest(technicianCordinates, customerLocation))
        

        #----------------------------------------
        feedbackObj = Feedbacks.objects.filter(leadID=leadObj)
        if len(feedbackObj) != 0:
            dataArray = []
            
            for eachFeedback in feedbackObj:
                data = {}
                data["leadID"] = str(eachFeedback.leadID)
                # here empID is the employee object and it has 
                # a field called empID
                data["empID"] = str(eachFeedback.empID.empID)
                data["feedback"] = eachFeedback.feedback
                data["createdAt"] = str(eachFeedback.createdAt)
                dataArray.append(data)
            lead['feedbacks'] = dataArray
        return success(lead)
    return fail("Error In Request")


@csrf_exempt
def getClosestTechnician(request):
    if request.method == "POST":
        positionData_list = []

        lead_id = request.POST.get("lead_id", None)
        if lead_id == '' or lead_id == None:
            return fail("lead ID hasn't provided")
        try:
            leadObj = Leads.objects.get(leadID=lead_id)
        except Exception as e:
            return fail("Lead doesn't exist")

        if leadObj.address != '':
            addr = leadObj.address.replace(" ", "+")
            api_key = 'AIzaSyCKrObWSq1_SI_Abkr71Rdo3pKx29KJGJM'
            uri = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=' + api_key
            response = req.get(uri)
            resp_json_payload = response.json()
            leadLocation = (resp_json_payload['results'][0]['geometry']['location'])

            try:
                loctnsObj = TechniciansLocation.objects.filter(isActive=True)
            except Exception as e:
                return fail("Something went wrong")

            if len(loctnsObj) == 0:
                return fail("No active technicians found")
            else:
                for loctnObj in loctnsObj:
                    eachRow = {}

                    eachRow['empID'] = loctnObj.empID
                    eachRow['latitude'] = loctnObj.latitude
                    eachRow['longitude'] = loctnObj.longitude

                    positionData_list.append(eachRow)


            closestAgent = closest(positionData_list, leadLocation)
            #This will return a dictionary contains empID so as latitude and longitude
            return success(closestAgent)
    return fail("Error in request")

    


def distance(lat1, lng1, lat2, lng2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lng2-lng1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'], v['lng'], p['lat'], p['lng']))



# v = {'lat': 39.7622290, 'lng': -86.1519750}
# print(closest(tempDataList, v))


@csrf_exempt
def updateTechniciansLocation(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)
        latitude = request.POST.get("latitude", None)
        longitude = request.POST.get("longitude", None)

        try:
            empObj = Employee.objects.get(empID=emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")
        
        try:
            loctnObj = TechniciansLocation.objects.get(empID=emp_id)
        except Exception as e:
            # if his location didn't exist before it will be an exception
            loctnObj = TechniciansLocation(empID=empObj, latitude=latitude, longitude=longitude)
            loctnObj.save()
        
        loctnObj.latitude = latitude
        loctnObj.longitude = longitude
        loctnObj.save()
        return success("Cordinates are saved")
    return fail("Error in request")


@csrf_exempt
def getTechniciansLocation(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)
        isWhole = request.POST.get("isWhole", None)

        if isWhole == '' or isWhole == 'false':
            if emp_id == '':
                return fail("You haven't provided employee id")
            try:
                empObj = Employee.objects.get(empID=emp_id)
            except Exception as e:
                return fail("Employee doesn't exist")

            try:
                loctnObj = TechniciansLocation.objects.get(empID=empObj)
            except Exception as e:
                return fail("No location data saved for this employee")

            cordinateData = {
                'empID': loctnObj.empID,
                'latitude': loctnObj.latitude,
                'longitude': loctnObj.longitude
            }
            return success(cordinateData)
        if isWhole == 'true':

            try:
                loctnsObj = TechniciansLocation.objects.filter(isActive=True)
            except Exception as e:
                return fail("Something went wrong")

            if len(loctnsObj) == 0:
                return fail("No active technicians found")
            else:
                positionData_list = []
                for loctnObj in loctnsObj:
                    eachRow = {}

                    eachRow['empID'] = loctnObj.empID
                    eachRow['latitude'] = loctnObj.latitude
                    eachRow['longitude'] = loctnObj.longitude

                    positionData_list.append(eachRow)
                return success(positionData_list)
    return fail("Error in request")


@csrf_exempt
def changeEmpPass(request):
    if request.method == "POST":
        emp_id = request.POST.get("id", None)
        newPassword = request.POST.get("newPassword", None)
        
        try:
            empObj = Employee.objects.get(id = emp_id)
        except Exception as e:
            print(e)
        empObj.password = newPassword
        empObj.save()
        return success("Password successfully changed.")
    return fail("Error in Request")


@csrf_exempt
def makeCall(request):
    if (request.method == "POST"):
        lead_id = request.POST.get("lead_id", None)
        emp_id = request.POST.get("emp_id", None)
        phone = request.POST.get("phone", None)

        if phone == "":
            return fail("Phone number is not provided")
        empObj = Employee.objects.get(empID=emp_id)
        leadObj = Leads.objects.get(leadID=lead_id)
        callObj = CallData(leadID=leadObj, empID=empObj, phone=phone)
        callObj.save()
        return success("Call has been placed")
    return fail("Error in request")

# @csrf_exempt
# def getCallReport(request):
#     if (request.method == "POST"):



@csrf_exempt
def leadDataFileParser(request):
    if (request.method == "POST"):
        myfile = request.FILES['dataFile']
        # fs = FileSystemStorage()

        folder="home/static/rawLeadFile"
        imagefile=FileSystemStorage(location=folder)
        imagesave=imagefile.save(myfile.name, myfile)

        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        data = pd.read_excel(folder + "/" + myfile.name)
        row, col = data.shape
        rows = []
        for i in range(row):
            email, fname, lname, address, phone, alternatePhone, pincode, source, purchaseDate = data.loc[i, ['email', 'fname', 'lname', 'address', 'phone', 'alternatePhone', 'pincode', 'source', 'purchaseDate']]
            lead = Leads(leadID = generateRandomLeadID(), email=email, fname=fname, lname=lname, address=address, phone=phone, alternatePhone=alternatePhone, pincode=pincode, source=source, purchaseDate=purchaseDate)
            rows.append(lead)

        try:
            Leads.objects.bulk_create(
                rows
            )
        except Exception as e:
            print(e)
            return fail("Lead upload failed")
        return success("completed upload")
    return fail("Error in request")

def generateRandomLeadID():
    randomID = 'LD' + '{0:06}'.format(random.randint(1, 100000))
    return randomID

# @csrf_exempt
# def getCallCount(request):
#     if (request.method=="POST"):
#         empid = request.POST.get("id",None)
#         if(empid != None):
#             try:
#                 employee = Employee.objects.get(id=empid)
#             except Exception as e:
#                 return fail("Employee Id Not Foud")
#             empObj = CallsPerDay.objects.filter(employee = employee , id = empid)
#             emp={}
#             emp['total']=empObj.totalCalls
#             emp['completed']=empObj.completedCalls
#             # return success(lead)
#             return success(emp)
#     return HttpResponse("Error In Request")

# @csrf_exempt
# def setCallCount(request):
#     if (request.method=="POST"):
#         empid = request.POST.get("id",None)

#         if(empid != None):
#             try:
#                 employee = Employee.objects.get(id=empid)
#             except Exception as e:
#                 return fail("Employee Id Not Foud")
#             empObj = CallsPerDay.objects.get(employee = employee)
#             count = empObj.completedCalls
#             count = count + 1
#             return success(lead)
#     return HttpResponse("Error In Request")
        
# @csrf_exempt
# def updateStatus(request):
#     if (request.method=="POST"):
#         id = request.POST.get("id",None)
#         status = request.POST.get("status",None)
#         comments = request.POST.get("comments",None)
#         if(id == None ):
#            return fail("No Id Found")
#         else:
#             lead = Customer.objects.get(id = id)
#             lead.status = status
#             lead.comments = comments
#             # lead = Customer(status = status, comments = comments)
#             lead.save()
#             return success("New Lead created!")
#     return HttpResponse("Error In Request")
