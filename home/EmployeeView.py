# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .views import success,fail
from .models import Employee, EmpTarget, Leads, Metrics, EmpStatus
from django.shortcuts import HttpResponse
import datetime
from django.utils import timezone
import random
from django.db import connection
from pprint import pprint
import pytz


@csrf_exempt
def createNewEmployee(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("email", None)
        address = request.POST.get("address", None)
        pincode = request.POST.get("pincode", None)
        role = request.POST.get("role", None)

        print(fname, lname, phone, email, address, pincode, role)
        if fname is '' or role is '' or phone is '' or email is '':
            return fail("Invalid details")

        if role == "Admin":
            role = "ad"
        if role == "Telecaller":
            role = "tc"
        if role == "Technician":
            role = "ts"
        if role == "QC":
            role = "qc"
        if role == "HR":
            role = "hr"
        if role == "TL":
            role = "tl"
        newEmpID = generateRandomempID()
        print(newEmpID)
        employee = Employee(empID = newEmpID, fname=fname, lname=lname, phone=phone, email=email, role=role, pincode = pincode)
        employee.save()
    return success(newEmpID)
    return fail("Error in request")

def displayAllEmployee(request):
    employees=Employee.objects.filter(isActive=True)
    print(employees)
    print("DATA IS OUTPUTTED OVER HERE")
    employee_list=[]
    print(len(employees))
    if(len(employees)==0):
        return fail("No employee in db")
    else:
        for i in range(len(employees)):
            emp={}
           
            emp['email']=employees[i].email
            emp['phone']=employees[i].phone
            emp['category']=employees[i].type
            emp['name']=employees[i].name
            emp['id']=employees[i].id
            emp['pincode']=employees[i].pincode
            employee_list.append(emp)

        return success(employee_list)

def displayAllEmployee_tech(request):
    print("*******yessssss")
    employees=Employee.objects.filter(isActive=True)
    print(employees)
    print("DATA IS OUTPUTTED OVER HERE")
    employee_list=[]
    print(len(employees))
    if(len(employees)==0):
        return fail("No employee in db")
    else:
        for i in range(len(employees)):
            emp={}
           
            emp['email']=employees[i].email
            emp['phone']=employees[i].phone
            emp['category']=employees[i].role
            emp['name']=employees[i].fname
            emp['id']=employees[i].id
            emp['pincode']=employees[i].pincode
            employee_list.append(emp)

        return success(employee_list)

@csrf_exempt
def addcallbacks(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname", None)
        empID = request.POST.get("empID", None)
        phone = request.POST.get("phone", None)
        appointmentDate= request.POST.get("appointmentDate", None)
        callbacks = Callbacks(empID = empID, fname=fname, phone=phone, appointmentDate=appointmentDate)
        callbacks.save()
    return success(newEmpID)
    return fail("Error in request")


def generateRandomempID():
    randomID = 'EMP' + '{0:06}'.format(random.randint(1, 100000))
    return randomID

@csrf_exempt
def getAllEmployees(request):
    employees=Employee.objects.all()
    employee_list=[]
    if (len(employees)==0):
        return fail("No employee in db")
    else:
        for i in range(len(employees)):
            emp={}
            emp['empID']=employees[i].empID
            emp['fname']=employees[i].fname
            emp['lname']=employees[i].lname
            emp['email']=employees[i].email
            emp['phone']=employees[i].phone
            emp['role']=employees[i].role
            emp['id']=employees[i].id
            emp['isActive']=employees[i].isActive
            emp['pincode']=employees[i].pincode
            try:
                imgUrl = employees[i].profile_logo.url
                emp['picture']=employees[i].profile_logo.url
            except Exception as e:
                print("No picture present")
            employee_list.append(emp)

        return success(employee_list)


@csrf_exempt
def getAllActiveEmployees(request):
    try:
        employees=Employee.objects.filter(isActive=True)
    except Exception as e:
        return fail("Some thing went wrong")
    employee_list=[]
    if (len(employees)==0):
        return fail("No employees active at the moment")
    else:
        for i in range(len(employees)):
            emp={}
            emp['fname']=employees[i].fname
            emp['lname']=employees[i].lname
            emp['email']=employees[i].email
            emp['phone']=employees[i].phone
            emp['address']=employees[i].address
            emp['role']=employees[i].role
            emp['id']=employees[i].id
            emp['pincode']=employees[i].pincode
            emp['picture']=employees[i].profile_logo.url
            employee_list.append(emp)

        return success(employee_list)


@csrf_exempt
def deactivateEmployee(request):
    if request.method =='POST':
        emp_id=request.POST.get("id", None)
        if emp_id == None or emp_id == '':
            return fail("Employee id not provided")
        try:
            empObj = Employee.objects.get(id = emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")
        empObj.isActive=False
        empObj.save()
        return success("Employee deactivated successfully")
    return fail("Error in request")


@csrf_exempt
def getSingleEmployee(request):
    if (request.method == "POST"):
        emp_id = request.POST.get("id", None)
        empObj = Employee.objects.get(empID=emp_id)
        employee = {}
        employee['empID'] = empObj.empID
        employee['fname'] = empObj.fname
        employee['lname'] = empObj.lname
        employee['email'] = empObj.email
        employee['phone'] = empObj.phone
        employee['address'] = empObj.address
        employee['isActive'] = empObj.isActive
        employee['pincode'] = empObj.pincode
        try:
            imgUrl = empObj.profile_logo.url
            employee['profilePicture'] = imgUrl
        except Exception as e:
            print("No picture present")
        employee['role'] = empObj.role
        return success(employee)
    return HttpResponse("Error In Request")

# This function used to change progress on calls and commits you have made
@csrf_exempt
def registerProgress(request):
    if request.method == "POST":
        # timeNow = datetime.datetime.now()
        timeNow = timezone.now()

        emp_id = request.POST.get("emp_id", None)
        action = request.POST.get("action", None)

        if emp_id is None or action is None:
            return fail("Necessary data haven't provided")

        # print(timeNow.date())
        # print(testTimeNow.date())

        try:
            empObj = Employee.objects.get(empID=emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")

        if action == 'call':
            try:
                metricsObj = Metrics.objects.filter(empID=empObj, createdAt__year=timeNow.year, createdAt__month=timeNow.month, createdAt__day=timeNow.day)
            except Exception as e:
                return fail("Something went wrong")
            
            if len(metricsObj) == 0:
                metricsObj = Metrics(empID=empObj, callCount=1, currDate=timeNow)
                metricsObj.save()
                return success("Progress for new day has been registered")
            else:
                metricsObj[0].createdAt = timeNow
                metricsObj[0].callCount = metricsObj[0].callCount + 1
                metricsObj[0].save()
                return success("Call count for the same day has been increased")
        if action == 'commit':
            try:
                metricsObj = Metrics.objects.filter(empID=empObj, createdAt__year=timeNow.year, createdAt__month=timeNow.month, createdAt__day=timeNow.day)
            except Exception as e:
                return fail("Something went wrong")
            
            if len(metricsObj) == 0:
                metricsObj = Metrics(empID=empObj, commitCount=1, currDate=timeNow)
                metricsObj.save()
                return success("Progress for new day has been registered")
            else:
                metricsObj[0].createdAt = timeNow
                metricsObj[0].commitCount = metricsObj[0].commitCount + 1
                metricsObj[0].save()
                return success("Commit count for the same day has been increased")
        if action == 'callback':
            try:
                metricsObj = Metrics.objects.filter(empID=empObj, createdAt__year=timeNow.year, createdAt__month=timeNow.month, createdAt__day=timeNow.day)
            except Exception as e:
                return fail("Something went wrong")
            
            if len(metricsObj) == 0:
                metricsObj = Metrics(empID=empObj, callbackCount=1, currDate=timeNow)
                metricsObj.save()
                return success("Progress for new day has been registered")
            else:
                metricsObj[0].createdAt = timeNow
                metricsObj[0].callbackCount = metricsObj[0].callbackCount + 1
                metricsObj[0].save()
                return success("Callback count for the same day has been increased")
    return fail("Error in request")


@csrf_exempt
def generateReport(request):
    if request.method == "POST":
        print()
        # timeNow = timezone.now()
        timeNow = datetime.datetime.now()

        emp_id = request.POST.get("emp_id", None)

        #daily or custom
        report_type = request.POST.get("report_type", None)

        from_date = request.POST.get("from_date", None)
        to_date = request.POST.get("to_date", None)

        #single employee or all employees
        report_for = request.POST.get("report_for", None)


        if report_for == 'single':

            if emp_id is '' or emp_id is None:
                return fail("Provide employee id")

            try: 
                print(emp_id)
                empObj = Employee.objects.get(empID=emp_id)
            except Exception as e:
                return fail("Employee doesn't exist")

            try:
                print(empObj.empID)
                empStatObj = EmpStatus.objects.filter(empID_id=empObj, date=str(timeNow.date()))

            except Exception as e:
                print(e)
                return fail("Status is not stored for this employee")

            if report_type == 'daily':
                try:
                    metricsObj = Metrics.objects.filter(empID=empObj, createdAt__year=timeNow.year, createdAt__month=timeNow.month, createdAt__day=timeNow.day)
                except Exception as e:
                    return fail("Something went wrong")
                else:
                    data_list = []
                    if len(metricsObj) == 0:
                        return fail("No records avialable")
                    else:
                        # although we are looping it assumed to be only one object in an array.
                        dataSet = {
                            "callCount": metricsObj[0].callCount,
                            "commitCount": metricsObj[0].commitCount,
                            "callbackCount": metricsObj[0].callbackCount,
                            "createdAt": str(metricsObj[0].createdAt),
                            "loginTime": empStatObj[0].loginTime,
                            "logoutTime": empStatObj[0].logoutTime
                        }
                        data_list.append(dataSet)
                    return success(data_list)

            if report_type == 'custom':
                # _from_date = '2019-03-30'
                # _to_date = '2019-04-04'
                if from_date == '' or from_date == None:
                    return fail("Please provide from and to dates")
                if to_date == '' or to_date == None:
                    return fail("Please provide from and to dates")

                fromDate = datetime.datetime.strptime(from_date, '%Y-%m-%d')
                toDate = datetime.datetime.strptime(to_date, '%Y-%m-%d')
                # formatted_from_date = pytz.utc.localize(from_date)
                # print(formatted_from_date.date)
                # to_date = datetime.datetime.strptime(_to_date, '%Y-%m-%d')
                # formatted_to_date = pytz.utc.localize(to_date)
                # print(formatted_to_date)

                try: 
                    empObj = Employee.objects.get(empID=emp_id)
                except Exception as e:
                    return fail("Employee doesn't exist")
                try:
                    # metricsObj = Metrics.objects.filter(empID=empObj, createdAt__lte=from_date.date(), createdAt__gt=to_date.date())
                    metricsObj = Metrics.objects.filter(empID=empObj, createdAt__range=(fromDate.date(), toDate.date()))
                except Exception as e:
                    return fail("Something went wrong")
                else:
                    if len(metricsObj) == 0:
                        return fail("No records avialable")
                    else:                        
                        # data list array has been introduced to make it front-end friendly
                        #$.each function likes to have an array.
                        data_list = []
                        callCount = 0
                        commitCount = 0
                        callbackCount = 0
                        for eachObj in metricsObj:
                            callCount = callCount + eachObj.callCount
                            commitCount = commitCount + eachObj.commitCount
                            callbackCount = callbackCount + eachObj.callbackCount

                        dataSet = {
                            "callCount": callCount,
                            "commitCount": commitCount,
                            "callbackCount": callbackCount
                        }
                        data_list.append(dataSet)
                        return success(data_list)

        if report_for == 'all':

            empObjs = Employee.objects.filter(role='tc')

            if len(empObjs) == 0:
                return fail("No employees in db")

            if report_type == 'daily':
                
                data_list = []

                for empObj in empObjs:
                    dataSet = {}
                    #get login information
                    try:
                        empStatObj = EmpStatus.objects.get(empID=empObj)
                    except Exception as e:
                        print("No record avaialable for this employee")
                    else:
                        dataSet["loginTime"] = empStatObj.loginTime
                        if empStatObj.logoutTime == None:
                            dataSet["logoutTime"] = ''
                        else:
                            dataSet["logoutTime"] = empStatObj.logoutTime
                    
                    #get metrices 
                    try:
                        metricsObj = Metrics.objects.filter(empID=empObj, createdAt__year=timeNow.year, createdAt__month=timeNow.month, createdAt__day=timeNow.day)
                    except Exception as e:
                        print("No record avaialable for this employee")
                    else:
                        if len(metricsObj) == 0:
                            return fail("No progress found in db")

                        dataSet['emp_id'] = metricsObj[0].empID.empID
                        dataSet['callCount'] = metricsObj[0].callCount
                        dataSet['commitCount'] = metricsObj[0].commitCount
                        dataSet['callbackCount'] = metricsObj[0].callbackCount
                            

                    data_list.append(dataSet)
                return success(data_list)

            if report_type == 'custom':
                # _from_date = '2019-03-30'
                # _to_date = '2019-04-04'
                if from_date == '' or from_date == None:
                    return fail("Please provide from and to dates")
                if to_date == '' or to_date == None:
                    return fail("Please provide from and to dates")

                fromDate = datetime.datetime.strptime(from_date, '%Y-%m-%d')
                toDate = datetime.datetime.strptime(to_date, '%Y-%m-%d')

                
                data_list = []
                for empObj in empObjs:

                    try:
                        metricsObj = Metrics.objects.filter(empID=empObj, createdAt__range=(fromDate.date(), toDate.date()))
                    except Exception as e:
                        return fail("Something went wrong")

                    if len(metricsObj) == 0:
                        print("No records avialable for this employee")

                    # print(len(metricsObj))

                    callCount = 0
                    commitCount = 0
                    callbackCount = 0
                    for eachObj in metricsObj:
                        callCount = callCount + eachObj.callCount
                        commitCount = commitCount + eachObj.commitCount
                        callbackCount = callbackCount + eachObj.callbackCount
                    dataSet = {
                        "emp_id": eachObj.empID.empID,
                        "callCount": callCount,
                        "commitCount": commitCount,
                        "callbackCount": callbackCount,
                        "loginTime": '',
                        "logoutTime": ''
                    }
                    data_list.append(dataSet)
                return success(data_list)

    return fail("Error in request")


        

        


@csrf_exempt
def updateEmployee(request):
    if request.method == "POST":
        emp_id = request.POST.get("id", None)
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("mail", None)
        pincode = request.POST.get("pincode", None)
        address = request.POST.get("address", None)
        image = request.FILES.get("profilePic",None)

        if emp_id == None or emp_id == '':
            return fail("Employee id is not provided")

        empObj = Employee.objects.get(empID = emp_id)
        if fname is not None:
            empObj.fname = fname
        if lname is not None:
            empObj.lname = lname
        if phone is not None:
            empObj.phone = phone
        if email is not None:
            empObj.email = email
        if pincode is not None:
            empObj.pincode = pincode
        if address is not None:
            empObj.address = address
        if image is not None:
            empObj.profilePicture= image
        empObj.save()
        return success("Employee information updated")
    return fail("Error in request")



@csrf_exempt
def uploadEmployeeProfilePic(request):
    print(request.POST)
    print(request.FILES)
    if(request.method=="POST"):
        id=request.POST.get("id", None)
        if id is not None:
            try:
                emp = Employee.objects.get(empID=id)
                emp.profilePicture=request.FILES['profile_pic']
                emp.save()
                return success("success")
                # return success("profile image saved at "+emp.profilePicture)
            except Exception as e:
                print(e)
                return fail("failed")
    return fail("Bad request")

@csrf_exempt
def setEmpTarget(request):
    if request.method=="POST":
        currDate = str(datetime.datetime.now().date())
        emp_id = request.POST.get("emp_id", None)
        if emp_id == None or emp_id == '':
            return fail("employee id hasn't provided")
        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            return fail("Employee Id Not Found")
        callTarget = request.POST.get("callTarget", None)
        commitTarget = request.POST.get("commitTarget", None)
        print(callTarget)
        print(commitTarget)
        # endDate = request.POST.get("endDate", None)

        # Just incase if they don't want to use the progress bar.
        if callTarget == None:
            callTarget = 0
        if commitTarget == None:
            commitTarget = 0
        try:
            targetObj =  EmpTarget.objects.get(empID = empObj)
        except Exception as e:
            # if no employee there in the table the try would fail.
            newTargetObj = EmpTarget()
            newTargetObj.empID = empObj
            newTargetObj.callTarget = callTarget
            newTargetObj.commitTarget = commitTarget
            newTargetObj.startDate = currDate
            # newTargetObj.endDate = endDate
            newTargetObj.save()
            return success("New employee target has been saved")
        # if the employee data already exist in the the table do this
        targetObj.empID = empObj
        targetObj.callTarget = callTarget
        targetObj.commitTarget = commitTarget
        targetObj.startDate = currDate
        # targetObj.endDate = endDate
        targetObj.save()
        return success("Target has been updated")
    return fail("Error in request")

@csrf_exempt
def getEmpTarget(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)
        if emp_id == None or emp_id == "":
            return fail("Employee Id hasn't provided")
        try:
            empObj = Employee.objects.get(empID=emp_id)
        except Exception as e:
            return fail("Employee doesn't exist")
        print(empObj)
        try:
            statObj = EmpTarget.objects.get(empID=empObj)
        except Exception as e:
            return fail("Employee has no target assinged")
        #Create a dic on his assigned target
        target = {}
        target["calls"] = statObj.callTarget
        target["commits"] = statObj.commitTarget
        target["startDate"] = statObj.startDate
        target["endDate"] = statObj.endDate

        return success(target)
    return fail("Error in request")


@csrf_exempt
def assignLeads(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id", None)
        leadIDs = request.POST.getlist("leadIDs[]", None)
        if emp_id == None or emp_id == '':
            return fail("Employee ID required")

        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            return fail("Employee does not exist")
        for i in leadIDs:
            lead=Leads.objects.get(leadID=i)
            print("@@@@@@@@@@@@")
            print(lead.assignee)
            lead.assignee=empObj
            lead.save()
        return success("Successfully assigned")
    return fail("Error in request")

        














