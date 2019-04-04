from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    empID = models.CharField(max_length=12, unique=True, default=None)
    phone = models.CharField(max_length=12, default=None)
    password = models.CharField(max_length=20, default='password')
    pincode = models.CharField(max_length=6, default="000000")
    email = models.CharField(max_length=30, default="None")
    address = models.CharField(max_length=500, default="None")
    role = models.CharField(max_length=5, default='tc')
    isActive = models.BooleanField(default=False)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    profile_logo = models.FileField(null=True)
    profilePicture = models.ImageField(null=True, upload_to="home/static/images/employee/")



#CATEGORIES 'eq'-EQUIPMENT, 'mn'-MACHINE , 'fl'-FILTER
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    description=models.TextField()
    product_id=models.CharField(max_length=30,unique=True)
    year=models.CharField(max_length=20)
    cost=models.IntegerField()
    category=models.CharField(max_length=2,default='mn')
    features=models.TextField(null=True)
    image_path=models.ImageField(blank=True)
    
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30 , default=None)
    email=models.CharField(max_length=30, default=None)
    mobile=models.CharField(max_length=10, default=None)
    alternativeMobile=models.CharField(max_length=10, default=None)
    address=models.CharField(max_length=300, default=None)
    pincode=models.CharField(max_length=6, default=None)
    #DEVICE NAME
    Equipment=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    isClient=models.BooleanField(default=False)
    land=models.CharField(max_length=100, default=None)
    comments=models.TextField(null=True)
    status=models.CharField(max_length=10, default="nyc")
    assign= models.BooleanField(default=False)
    city=models.CharField(max_length=20, blank=True)
    latitude=models.CharField(max_length=20, blank=True)
    longitude=models.CharField(max_length=20, blank=True)



#EMPLOYEE ROLE
#'tc'->telecaller 
#'tn'->technician
#'ts'->tech support
#'ad'->admin

# class Technicians(models.Model):
#     employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
#     ticket_id = models.FloatField(null=True, blank=True, default=None)
#     max_aasginment = models.FloatField(null=True, blank=True, default=None)
#     ticket_status = models.BooleanField(default=False)
#     ticket_assigned_date

class Callbacks(models.Model):
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=12, default=None)
    fname = models.CharField(max_length=12, default=None)
    appointmentDate = models.CharField(max_length=12, default=None)

class EmpStatus(models.Model):
    id = models.AutoField(primary_key=True)
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    loginTime = models.CharField(max_length=10, null=True)
    logoutTime = models.CharField(max_length=10, null=True)
    date = models.CharField(max_length=10, null=True)
    isPause = models.BooleanField(default=False)
    pauseTime = models.CharField(max_length=10, null=True)


class Notifications(models.Model):
    id = models.AutoField(primary_key=True)
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    time = models.CharField(max_length=10, null=True)
    date = models.CharField(max_length=10, null=True)
    noteForAll = models.BooleanField(default=False)
    noteType = models.TextField(null=True)
#noteType=notfication -> for employees page
#noteType=issue -> for admin page

class EmpTarget(models.Model):
    id = models.AutoField(primary_key=True)
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    callTarget = models.IntegerField()
    commitTarget = models.IntegerField()
    startDate = models.CharField(max_length=10, null=True)
    endDate = models.CharField(max_length=10, null=True)

# Create your models here.



# class Customers(models.Model):
#     custID = models.CharField(max_length=30, default=None, primary_key=True)
#     fname = models.CharField(max_length=30, default=None)
#     lname = models.CharField(max_length=20, default=None)
#     email = models.CharField(max_length=30, default=None)
#     mobile = models.CharField(max_length=12, default=None)
#     alternativeMobile = models.CharField(max_length=12, default=None)
#     address = models.CharField(max_length=300, default=None)
#     pincode = models.CharField(max_length=6, default=None)
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


class Leads(models.Model):
    leadID = models.CharField(max_length=30, default=None, primary_key=True)
    fname = models.CharField(max_length=100, default=None)
    address = models.TextField(default=None, null=True)
    email = models.EmailField(default=None, null=True)
    phone = models.CharField(max_length=12, unique=True, default=None, null=True)
    alternatePhone = models.CharField(max_length=12, default=None, null=True)
    purchaseDate = models.CharField(max_length=12, null=True)
    pincode = models.CharField(max_length=6, default="000000", null=True)
    source = models.CharField(max_length=40, default=None, null=True)
    product = models.CharField(max_length=30, default=None, null=True)
    appointmentDate = models.CharField(max_length=12, default=None, null=True)
    comments = models.TextField(null=True)
    callAction = models.CharField(max_length=4, default='df', null=True)
    assignee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    createdDate = models.DateTimeField(default=timezone.now)
    isContacted = models.BooleanField(default=False)
    isInterested = models.BooleanField(default=False)

class CallData(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    leadID = models.ForeignKey(Leads, on_delete=models.SET_NULL, null=True)
    empID = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    duration = models.DurationField(null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=12, default=None)
    remarks = models.TextField(default=None, null=True)
    recordLink = models.TextField(null=True)

class Metrics(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    empID = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    callCount = models.IntegerField(default=0, null=True)
    commitCount = models.IntegerField(default=0, null=True)
    callbackCount = models.IntegerField(default=0, null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    currDate = models.DateTimeField(null=True)

class Feedbacks(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    feedback = models.TextField(default=None)
    leadID = models.ForeignKey(Leads, on_delete=models.SET_NULL, null=True)
    empID = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(default=timezone.now)


class Complaints(models.Model):
    bookingID = models.CharField(max_length=10, default=None, primary_key=True)
    technicianID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    customerID = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True)
    createdDate = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100, default=None)
    address = models.TextField(default=None)
    pincode = models.CharField(max_length=6, default="000000")
    appointmentTime = models.DateField(default=None)
    subject = models.CharField(max_length=100)
    problem_description = models.TextField()
    recording_data_url = models.TextField()
    severity = models.IntegerField(validators=[MaxValueValidator(4)], default=1)
    isActive = models.BooleanField(default=True)


#status INprogress='ip'. and completed='cp'
class CustomerEmployee(models.Model):
    customer= models.ForeignKey(Customer, on_delete = models.SET_NULL,null=True)
    employee= models.ForeignKey(Employee, on_delete = models.SET_NULL,null=True)
    dateAssigned = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=15, default="ip")

#calls count per day
class CallsPerDay(models.Model):
    id = models.AutoField(primary_key=True)
    dateAssigned = models.DateField(auto_now_add = True)
    employee = models.ForeignKey(Employee, on_delete = models.SET_NULL,null=True)
    totalCalls = models.IntegerField(default = 100)
    completedCalls = models.IntegerField(default = 0)


#BOOKING IS ALSO REFERRED TO AS TICKET
class CurrentBooking(models.Model):
    bookingId=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    technician=models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True)
    problem_description=models.TextField()
    request_date=models.DateField(auto_now_add=True)
    recording_data_url=models.TextField()



#THIS DATA IS FETCHED FROM CURRENT BOOKING WHILE BOOKING IS EXECUTED
class previousBooking(models.Model):
    id = models.AutoField(primary_key=True)
    bookingId=models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    technician = models.ForeignKey(Employee, on_delete=models.CASCADE)
    problem_description = models.TextField()
    request_date = models.DateField()
    cost=models.FloatField(default=0.0);
    recording_data_url = models.TextField()
    completed_date=models.DateField(auto_now_add=True)

#Jayanagar->jaya
class Inventory(models.Model):
    id=models.AutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    goDown=models.CharField(max_length=5)

#Removing stock from inventory and handing over to the technician
class TechnicianStock(models.Model):
    sid=models.AutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    technician=models.ForeignKey(Employee,on_delete=models.CASCADE)
    qty=models.IntegerField()
    branch=models.CharField(max_length=5)

#SEPERATE TABLE NEED TO BE DEVELOPED FOR CUSTOMER AND EQUIPMENT RELATION
#BECAUSE ONE CUSTOMER MAY HAVE MULTIPLE EQUIPMENT WITH HIM
#IN CASE THAT THE CUSTOMER IS NOT A CLIENT THE DEVICE WHICH HE ENQUIRED FOR IS PUT IN
# STATUS nyc->not_yet_called nas->not_answered crs->call_resheduled nin->not_intrested 
    # inr->intrested nav->not_available










