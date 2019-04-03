from django.shortcuts import render,HttpResponse
# from home.models import Employee,Customer,CurrentBooking,Product
from home.models import Employee, Customer, Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json



#ANDROID LOGIN
@csrf_exempt
def login(request):
    if(request.method=='POST'):
        phone=request.POST.get("username",None)
        password=request.POST.get("password",None)
        if(phone==None and password==None):
            fail("Invalid credentials")
        else:
            technician_data = Employee.objects.filter(phone=phone, password=password, type='tn')
            if (len(technician_data) > 1):
                return HttpResponse("User Valid")
            else:
                return HttpResponse("User Invalid")

    return HttpResponse("Login is successful")


#TECHNICIAN REGISTRATION
@csrf_exempt
def registration(request):
    if(request.method=='POST'):
        #FETCH ALL DATA FROM THE USER
        phone,password,pincode,username=request.POST.get("phone",None),request.POST.get("password",None),request.POST.get("pincode",None),request.POST.get("username",None)
        #VALIDATE IF ALL THE DATA EXISTS
        print(phone)
        print(password)
        print(pincode)
        print(username)
        if(phone==None and password==None and pincode==None and username==None):
            return fail("invalid request")
        else:
            try:
                technician=Employee(phone=phone,password=password,name=username,pincode=pincode, type='tn')
                technician.save()
                return success("New user registered")
            except:
                return fail("database error")
    return HttpResponse("Invalid page")



def success(message):
    output = {}
    print("inside sucess")
    print(message)
    output["result"] = "success"
    output["description"] = message
    return HttpResponse(json.dumps(output))

def fail(message):
    output={}
    output["result"] = "fail"
    output["description"] = message
    return HttpResponse(json.dumps(output))


#changes made here for tesint purpose only



#REGISTER BOOKING
@csrf_exempt
def CustomerProblemRegistration(request):
    if(request.method=="POST"):
        print("hello")
        #userRelated data
        name,address,devicename,pincode=request.POST.get('name',None),request.POST.get('address',None),request.POST.get('devicename',None),request.POST.get("pincode",None)
        problem_description=request.POST.get('problem',None)

        print(name)
        print(address)
        print(devicename)
        print(pincode)
        print(problem_description)
        if(name==None and address==None and devicename==None and pincode==None and problem_description==None):
            return fail("Invalid data")
        else:
            # device problem registration
            print("creating customer")
            customer = Customer(name=name, address=address, DeviceName=devicename, pincode=pincode)
            customer.save()
            print("customer created")
            print(customer.id)
            if (customer.id >= 0):
                ticket = CurrentBooking(problem_description=problem_description, cid=customer.id)
                ticket.save()
                ticket_details = {}
                ticket_details['ticket_id'] = ticket.id
                ticket_details['resp'] = "New ticket raised"
                return success("ticke is hosted")
    else:
        return fail("post operation not required")

    print("invalid page option")
    return HttpResponse("Invalid page")


def displayAllTickets(request):
    currentBooking=CurrentBooking.objects.all()
    for i in range(len(currentBooking)):
        ticket={}




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

    #    return fail("No Booking to show")
@csrf_exempt
def getFullDetails(request):
    print(request.POST)
    if(request.method=="POST"):
        id=request.POST.get("id")
        print(id)
        import json
        data=json.loads(id)

        print(data)
        return success("cool");
    else:
        return fail("invalid data")




