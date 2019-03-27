# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .views import success,fail
from .models import Employee, EmpTarget, Leads
from django.shortcuts import HttpResponse
import datetime
import random


@csrf_exempt
def createNewEmployee(request):
    if (request.method=="POST"):
        fname = request.POST.get("fname",None)
        lname = request.POST.get("lname",None)
        phone = request.POST.get("phone",None)
        email = request.POST.get("email",None)
        address = request.POST.get("address", None)
        pincode = request.POST.get("pincode", None)
        role = request.POST.get("role", None)

        print(fname, lname, phone, email, address, pincode, role)
        if fname==None or role==None or phone==None or email==None:
           return fail("Invalid details")
        else:
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
            newEmpID = generateRandomEmployeeID()
            employee = Employee(empID = newEmpID, fname=fname, lname=lname, phone=phone, email=email, role=role, pincode = pincode)
            employee.save()
        return success(newEmpID)
    return fail("Error in request")

def generateRandomEmployeeID():
    randomID = 'EMP' + '{0:06}'.format(random.randint(1, 100000))
    return randomID

@csrf_exempt
def getAllEmployees(request):
    employees=Employee.objects.all()
    employee_list=[]
    print(len(employees))
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
            print("------------------is active is ------------")
            print(employees[i].isActive)
            emp['pincode']=employees[i].pincode
            try:
                imgUrl = employees[i].profile_logo.url
                emp['picture']=employees[i].profile_logo.url
            except Exception as e:
                print("no picture present")
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

@csrf_exempt
def updateEmployee(request):
    if (request.method == "POST"):
        emp_id = request.POST.get("id", None)
        fname = request.POST.get("fname", None)
        lname = request.POST.get("lname", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("mail", None)
        pincode = request.POST.get("pincode", None)
        address = request.POST.get("address", None)
        image=request.FILES.get("profilePic",None)

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
        print(emp_id)
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
            targetObj =  EmpTarget.objects.get(employeeID = empObj)
        except Exception as e:
            # if no employee there in the table the try would fail.
            newTargetObj = EmpTarget()
            newTargetObj.employeeID = empObj
            newTargetObj.callTarget = callTarget
            newTargetObj.commitTarget = commitTarget
            newTargetObj.startDate = currDate
            # newTargetObj.endDate = endDate
            newTargetObj.save()
            return success("New employee target has been saved")
        # if the employee data already exist in the the table do this
        targetObj.employeeID = empObj
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
            statObj = EmpTarget.objects.get(employeeID=empObj)
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
        # currDate = str(datetime.datetime.now().date())
        emp_id = request.POST.get("emp_id", None)
        leadIDs = request.POST.getlist("leadIDs[]", None)
        print(leadIDs)

        if emp_id == None or emp_id == '':
            return fail("Employee ID required")

        try:
            empObj = Employee.objects.get(empID = emp_id)
        except Exception as e:
            return fail("Employee does not exist")

        # leads = Leads.objects.filter(id__range(startRow, endRow))
        leads = Leads.objects.filter(leadID__in=leadIDs).update(assignee = empObj)
        # for lead in leads:
        #     lead.assignee = empObj
        # lead.save()
        return success("Successfully assigned")
    return fail("Error in request")

        














