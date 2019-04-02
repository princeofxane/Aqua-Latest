from django.shortcuts import render,HttpResponse
from .models import *
# from .models import Employee,Customer,CurrentBooking,Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from .views import fail, success

# REGISTER BOOKING
@csrf_exempt
def CustomerProblemRegistration(request):
    if (request.method == "POST"):
        print("hello")
        # userRelated data
        fname, lname, email = request.POST.get('fname', None), request.POST.get('lname', None), request.POST.get(
            'email', None)
        mobile, altermobile = request.POST.get("phone", None), request.POST.get('alter', None)
        address, devicename, pincode = request.POST.get('address', None), request.POST.get('device',
                                                                                           None), request.POST.get(
            'pincode', None)
        problem_description = request.POST.get('problem', None)
        land = request.POST.get('land', None)
        city, cityLng, cityLat = request.POST.get('city', None), request.POST.get('cityLng', None), request.POST.get(
            'cityLat', None)
        print(fname)
        print(lname)
        print(email)
        print(mobile)
        print(altermobile)
        print(address)
        print(devicename)
        print(pincode)
        print(problem_description)
        if (fname == None and address == None and devicename == None and pincode == None and problem_description == None and city == None and cityLng == None and cityLat == None):
            return fail("Invalid data")
        else:
            # device problem registration
            prod = Product.objects.get(product_id=devicename)
            print(prod)
            print("creating customer")
            customer = Customer(fname=fname, lname=lname, email=email, mobile=mobile, alternativeMobile=altermobile,
                                address=address, pincode=pincode, Equipment=prod, isClient=True, land=land, city=city,
                                latitude=cityLat, longitude=cityLng)

            customer.save()
            print("customer created")
            print(customer.id)
            current=CurrentBooking(problem_description=problem_description, customer=customer)
            current.save()
            return success("Booking completed")
            # if customer is not None:
            #     ticket_details=checkTech(customer,problem_description)
            #     if ticket_details is not None:
            #         return success(ticket_details)
            #     else:
            #         return fail("No technician found for your search")




    else:
        return fail("post operation is required")

    print("invalid page option")
    return HttpResponse("Invalid page")


def hostTicket(customer, problem_description, id, tech):
    if (id >= 0):
        ticket = CurrentBooking(problem_description=problem_description, customer=customer, technician=tech)
        ticket.save()
        return ticket.bookingId


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


@csrf_exempt
def existCustomerProblemRegistration(request):
    if (request.method == "POST"):
        print("hello")
        # userRelated data
        problem_description = request.POST.get('problem', None)
        cid = request.POST.get('cid', None)
        print("This is problem", problem_description)
        print(problem_description)
        if (problem_description == None and cid == None):
            return fail("Invalid data")
        else:
            customer=Customer.objects.get(id=cid)
            current=CurrentBooking(problem_description=problem_description, customer=customer)
            current.save()
            return success("successfully added");
                # ticket_details=checkTech(customer,problem_description)
                # if ticket_details is not None:
                #     return success(ticket_details)
                # else:
                #     return fail("No technician found for your search")



    else:
        return fail("post operation is required")

    print("invalid page option")
    return HttpResponse("Invalid page")


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