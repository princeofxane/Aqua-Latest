from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
from .views import success,fail
from .models import Customer, Employee, Leads, EmpStatus, Product
import random


@csrf_exempt
def addNewCustomer(request):
    if (request.method == "POST"):
        fname = request.POST.get("fname",None)
        lname = request.POST.get("lname",None)
        mobile = request.POST.get("mobile",None)
        email = request.POST.get("email",None)
        address = request.POST.get("address",None)
        pincode = request.POST.get("pincode",None)
        productID = request.POST.get("productID", None)
        alternativeMobile = request.POST.get("alternativeMobile",None)
        try:
            prodObj = Product.objects.get(id = productID)
        except Exception as e:
            return fail("Product doesn't exist")
        newCustID = generateRandomID()
        customer = Customers(custID = newCustID, fname = fname, lname = lname, mobile = mobile, email = email,
            address = address, pincode = pincode, alternativeMobile = alternativeMobile, product = prodObj)
        customer.save()
        return success("New customer created!")
    return fail("Error in request")

@csrf_exempt
def deleteCustomer(request):
    if request.method == "POST":
        cust_id = request.POST.get("cust_id", None)
        try:
            custObj = Customers.objects.get(custID=cust_id)
        except Exception as e:
            return fail("Customer doesn't exist")
        custObj.delete()
        return success("Customer has been successfully deleted")
    return fail("Error in request")

@csrf_exempt
def updateCustomer(request):
    if(request.method == "POST"):
        cust_id = request.POST.get("cust_id", None)
        prod_id = request.POST.get("prod_id", None)
        fname = request.POST.get("fname",None)
        lname = request.POST.get("lname",None)
        mobile = request.POST.get("mobile",None)
        email = request.POST.get("email",None)
        address = request.POST.get("address",None)
        pincode = request.POST.get("pincode",None)
        productID = request.POST.get("productID", None)
        alternativeMobile = request.POST.get("alternativeMobile",None)
        try:
            custObj = Customers.objects.get(custID = cust_id)
        except Exception as e:
            return fail("Customer doesn't exist")
        
        if fname is not None:
            custObj.fname = fname
        if lname is not None:
            custObj.lname = lname
        if mobile is not None:
            custObj.mobile = mobile
        if email is not None:
            custObj.email = email
        if address is not None:
            custObj.address = address
        if pincode is not None:
            custObj.pincode = pincode
        if productID is not None:
            try:
                prodObj = Product.objects.get(id=prod_id)
            except Exception as e:
                return fail("Product doesn't exist")
            custObj.product = prodObj
        return success("Customer has been updated")
    return fail("Error in request")
        
@csrf_exempt
def getSingleCustomer(request):
    if(request.method == "POST"):
        cust_id = request.POST.get("cust_id", None)
        if cust_id == None or cust_id == "":
            return fail("Customer id hasn't provided")
        try:
            custObj = Customers.objects.get(custID = cust_id)
        except Exception as e:
            return fail("Customer doesn't exist")
        #Get the product as well
        customer = {}
        customer["fname"] = custObj.fname
        customer["lname"] = custObj.lname
        customer["email"] = custObj.email
        customer["mobile"] = custObj.mobile
        customer["alternativeMobile"] = custObj.alternativeMobile
        customer["address"] = custObj.address
        customer["pincode"] = custObj.pincode
        customer["address"] = custObj.address
        customer["product_id"] = custObj.product.id
        customer["product_name"] = custObj.product.name
        customer["product_description"] = custObj.product.description
        customer["product_builtYear"] = custObj.product.builtYear
        customer["product_cost"] = custObj.product.cost
        customer["product_category"] = custObj.product.category
        print(customer)
        return success(customer)
    return fail("Error in request")
        
# @csrf_exempt
# def getSingleCustomer(request):
#     if (request.method=="POST"):
#         custID = request.POST.get("id",None)
#         custObj=Customers.objects.get(id = custID)
#         customer={}
#         customer['fname']=custObj.fname
#         customer['lname']=custObj.lname
#         customer['email']=custObj.email
#         customer['mobile']=custObj.phone
#         customer['alternativeMobile']=custObj.alternativeMobile
#         customer['address']=custObj.address
#         customer['pincode']=custObj.pincode
#         return success(customer)
#     return HttpResponse("Error In Request")

def generateRandomID():
    randomID = 'CS' + '{0:06}'.format(random.randint(1, 100000))
    return randomID
