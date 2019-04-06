from django.test import TestCase

# from .models import Employee,Customer,Product,CustomerEmployee, CallsPerDay, Leads
from .models import Employee, Customer, Product, Leads
# Create your tests here.

def fill_database_with_dummy_values():
    addEmployees()
    # addProducts()
    # addCustomers()
    # addDummyLeads()
    # addCustomerEmployeeRelation()

def cleanDatabase():
    Employee.objects.all().delete()
    Product.objects.all().delete()
    # Customers.objects.all().delete()


def addEmployees():
    #     EMPLOYEE INSERTION PROCEDURE
    emp1 = Employee(empID=1000, phone='8483800288', password='password', pincode='560077', email='drake.penn@gmail.com', role='tn', fname='drake', lname='penn')
    emp1.save()

    emp2 = Employee(empID=1001, phone='8483800288', password='password', pincode='560077', email='bob.thomas@gmail.com', role='tc', fname='bob', lname='thomas')
    emp2.save()

    emp3 = Employee(empID=1002, phone='8483800288', password='password', pincode='560077', email='michale.john@gmail.com', role='tc', fname='michale', lname='john')
    emp3.save()

    emp4 = Employee(empID=1003, phone='8483800288', password='password', pincode='560077', email='fred.durst@gmail.com', role='ad', fname='fred', lname='durst')
    emp4.save()

    print("employees has been added")

# def addProducts():
#     #    PRODUCT TABLE INSERTION
#     product = Product(name="Aqua Phobia", description="Twin UI filter protection", product_id="AQUA2018PD011",
#                       cost=15000, year='2018', features='Anti bacteria resistal ions')
#     product.save()

#     product = Product(name="Aqua Fin", description="Multi heating level ", product_id="AQUA2017PD022",
#                       cost=13000,
#                       year='2017', features='Anti bacteria resistal ions')
#     product.save()
#     product = Product(name="Aqua milton", description="Twin UI filter protection", product_id="AQUA2018pd012",
#                       cost=5000,
#                       year='2003', features='Anti bacteria resistal ions')
#     product.save()

# def addCustomers():
#     cust=Customer(id=1000000 ,fname='Navya',lname="reddy",email='navya.reddy@gmail.com',phone='6361567775',pincode='560078',address='J.p nagar 1st phase'
#                   ,alternativephone='',land='Sindoor convention hall')
#     cust.save()
#     cust = Customer(fname='Guntur', lname="Shashi", email='guntur.shashi@gmail.com', phone='6361567773', pincode='560078',
#                     address='J.p nagar 1st phase'
#                     , alternativephone='',land='Bangalore central')
#     cust.save()
#     cust = Customer(fname='Salman', lname="khan", email='saleman.khan@gmail.com', phone='9008522228', pincode='560078',
#                     address='J.p nagar 1st phase'
#                     , alternativephone='',land="gopalan mall")
#     cust.save()

# def addCallsHistories(id):
#     calls = CallsPerDay(id = 1002, totalCalls = 50, completedCalls = 40)


# def addCustomerEmployeeRelation():
#     ce=CustomerEmployee(customer=Customer.objects.get(fname='Navya', lname='reddy'),employee=Employee.objects.get(phone='8686168832'))
#     ce.save()
#     ce = CustomerEmployee(customer=Customer.objects.get(fname='Guntur', lname='Shashi'),
#                           employee=Employee.objects.get(phone='8686168832'))
#     ce.save()



# def displayLeads(id):
#     emp=Employee.objects.get(id=id)
#     ce=CustomerEmployee.objects.filter(employee=emp)
#     for row in ce:
#         print(row.employee.name+"-->"+row.customer.fname)




def addDummyLeads():
    #     This function add dummy leads
    
    emp1 = Leads(leadID='LD222777', fname='Matilde', lname='Tym', address='5460 Morningstar Drive', email='frew0@smh.com.au', phone='2552611487', purchaseDate='1/18/2019', pincode='346050')
    emp1.save()

    emp2 = Leads(leadID='LD222888', fname='Averill', lname='Mather', address='4 Vidon Lane', email='amather1@networkadvertising.org', phone='6094929496', purchaseDate='1/18/2019', pincode='346050')
    emp2.save()

    emp3 = Leads(leadID='LD222999', fname='Rad', lname='TymLidgerton', address='7 Badeau Parkway', email='rlidgerton2@issuu.com', phone='3501947315', purchaseDate='1/18/2019', pincode='346050')
    emp3.save()

    emp4 = Leads(leadID='LD333111', fname='Chrystel', lname='Saunier', address='7 Hooker Park', email='csaunier3@livejournal.com', phone='8735251497', purchaseDate='1/18/2019', pincode='346050')
    emp4.save()

    emp5 = Leads(leadID='LD333222', fname='Matilde', lname='Tym', address='33572 Coleman Park', email='bbaudinot4@i2i.jp', phone='8388609739', purchaseDate='1/18/2019', pincode='346050')
    emp5.save()

    emp6 = Leads(leadID='LD111111', fname='Barrie', lname='Baudinot', address='19 Esch Center', email='mpagett5@nature.com', phone='5806994835', purchaseDate='1/18/2019', pincode='346050')
    emp6.save()

    emp7 = Leads(leadID='LD222222', fname='Mercedes', lname='Pagett', address='6 Browning Lane', email='cmorilla6@dropbox.com', phone='6547662886', purchaseDate='1/18/2019', pincode='346050')
    emp7.save()

    emp8 = Leads(leadID='LD333333', fname='Clemmie', lname='Morilla', address='0 Harper Crossing', email='eborghese7@goodreads.com', phone='6804954610', purchaseDate='1/18/2019', pincode='346050')
    emp8.save()

    emp9 = Leads(leadID='LD444444', fname='Elmore', lname='Borghese', address='3330 Tomscot Point', email='tjills8@skype.com', phone='2739777624', purchaseDate='1/18/2019', pincode='346050')
    emp9.save()

    emp10 = Leads(leadID='LD555555', fname='Tedmund', lname='Jills', address='77 Sutteridge Crossing', email='ilagden9@friendfeed.com', phone='2658504398', purchaseDate='1/18/2019', pincode='346050')
    emp10.save()

    emp11 = Leads(leadID='LD666666', fname='Iosep', lname='Lagden', address='	37 Fisk Avenue', email='ffraina@indiatimes.com', phone='3814338584', purchaseDate='1/18/2019', pincode='346050')
    emp11.save()

    emp12 = Leads(leadID='LD777777', fname='Floyd', lname='Frain', address='392 Grim Trail', email='kkilkennyb@reverbnation.com', phone='3255641713', purchaseDate='1/18/2019', pincode='346050')
    emp12.save()

    emp13 = Leads(leadID='LD888888', fname='Krisha', lname='Kilkenny', address='65 Memorial Trail', email='ajacmardc@issuu.com', phone='2998756964', purchaseDate='1/18/2019', pincode='346050')
    emp13.save()

    emp14 = Leads(leadID='LD999999', fname='Arluene', lname='Jacmard', address='02852 Annamark Trail', email='atoore@feedburner.com', phone='6229489677', purchaseDate='1/18/2019', pincode='346050')
    emp14.save()

    emp15 = Leads(leadID='LD111222', fname='Alexa', lname='Kedie', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='7846648659', purchaseDate='1/18/2019', pincode='346050')
    emp15.save()

    emp16 = Leads(leadID='LD111333', fname='Adele', lname='McClaurie', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='3922641255', purchaseDate='1/18/2019', pincode='346050')
    emp16.save()

    emp17 = Leads(leadID='LD111444', fname='Jill', lname='Croux', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2814691320', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp17.save()

    emp18 = Leads(leadID='LD111555', fname='Rodie', lname='Orans', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='5569652199', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp18.save()

    emp19 = Leads(leadID='LD111666', fname='Conney', lname='Coggill', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1764097965', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp19.save()

    emp20 = Leads(leadID='LD111777', fname='Caroline', lname='Joutapavicius', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2735005958', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp20.save()

    emp21 = Leads(leadID='LD111888', fname='Ase', lname='Helix', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2768394890', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp21.save()

    emp22 = Leads(leadID='LD111999', fname='Florian', lname='Lemery', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1836576114', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp22.save()

    emp23 = Leads(leadID='LD222111', fname='Barbra', lname='Clissol', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='4749117151', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp23.save()

    emp24 = Leads(leadID='LD222333', fname='Koral', lname='Snelling', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='3986912324', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp24.save()

    emp25 = Leads(leadID='LD222444', fname='Sadella', lname='Ewbanke', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9371354173', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp25.save()

    emp26 = Leads(leadID='LD222555', fname='Johannah', lname='Revey', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='6573158554', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp26.save()

    emp27 = Leads(leadID='LD222666', fname='Sissy', lname='MacFadden', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1371568137', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp27.save()

    print("Dummy leads saved")



def addProduct():
    product=Product(name="filter",description="for filtering water",builtYear="2019",cost=3000,category="sp")
    product.save()
    product=Product(name="purifier",description="for filtering water",builtYear="2019",cost=3000,category="sp")
    product.save()



def addDummyLeads2():
    #     This function add dummy leads
    
    emp1 = Leads(leadID='LD222777', fname='Matilde', address='5460 Morningstar Drive', email='frew0@smh.com.au', phone='2552611487', purchaseDate='1/18/2019', pincode='346050')
    emp1.save()

    emp2 = Leads(leadID='LD222888', fname='Averill', address='4 Vidon Lane', email='amather1@networkadvertising.org', phone='6094929496', purchaseDate='1/18/2019', pincode='346050')
    emp2.save()

    emp3 = Leads(leadID='LD222999', fname='Rad', address='7 Badeau Parkway', email='rlidgerton2@issuu.com', phone='3501947315', purchaseDate='1/18/2019', pincode='346050')
    emp3.save()

    emp4 = Leads(leadID='LD333111', fname='Chrystel', address='7 Hooker Park', email='csaunier3@livejournal.com', phone='8735251497', purchaseDate='1/18/2019', pincode='346050')
    emp4.save()

    emp5 = Leads(leadID='LD333222', fname='Matilde', address='33572 Coleman Park', email='bbaudinot4@i2i.jp', phone='8388609739', purchaseDate='1/18/2019', pincode='346050')
    emp5.save()

    emp6 = Leads(leadID='LD111111', fname='Barrie', address='19 Esch Center', email='mpagett5@nature.com', phone='5806994835', purchaseDate='1/18/2019', pincode='346050')
    emp6.save()

    emp7 = Leads(leadID='LD222222', fname='Mercedes', address='6 Browning Lane', email='cmorilla6@dropbox.com', phone='6547662886', purchaseDate='1/18/2019', pincode='346050')
    emp7.save()

    emp8 = Leads(leadID='LD333333', fname='Clemmie', address='0 Harper Crossing', email='eborghese7@goodreads.com', phone='6804954610', purchaseDate='1/18/2019', pincode='346050')
    emp8.save()

    emp9 = Leads(leadID='LD444444', fname='Elmore', address='3330 Tomscot Point', email='tjills8@skype.com', phone='2739777624', purchaseDate='1/18/2019', pincode='346050')
    emp9.save()

    emp10 = Leads(leadID='LD555555', fname='Tedmund', address='77 Sutteridge Crossing', email='ilagden9@friendfeed.com', phone='2658504398', purchaseDate='1/18/2019', pincode='346050')
    emp10.save()

    emp11 = Leads(leadID='LD666666', fname='Iosep', address='	37 Fisk Avenue', email='ffraina@indiatimes.com', phone='3814338584', purchaseDate='1/18/2019', pincode='346050')
    emp11.save()

    emp12 = Leads(leadID='LD777777', fname='Floyd', address='392 Grim Trail', email='kkilkennyb@reverbnation.com', phone='3255641713', purchaseDate='1/18/2019', pincode='346050')
    emp12.save()

    emp13 = Leads(leadID='LD888888', fname='Krisha', address='65 Memorial Trail', email='ajacmardc@issuu.com', phone='2998756964', purchaseDate='1/18/2019', pincode='346050')
    emp13.save()

    emp14 = Leads(leadID='LD999999', fname='Arluene', address='02852 Annamark Trail', email='atoore@feedburner.com', phone='6229489677', purchaseDate='1/18/2019', pincode='346050')
    emp14.save()

    emp15 = Leads(leadID='LD111222', fname='Alexa', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='7846648659', purchaseDate='1/18/2019', pincode='346050')
    emp15.save()

    emp16 = Leads(leadID='LD111333', fname='Adele', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='3922641255', purchaseDate='1/18/2019', pincode='346050')
    emp16.save()

    emp17 = Leads(leadID='LD111444', fname='Jill', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2814691320', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp17.save()

    emp18 = Leads(leadID='LD111555', fname='Rodie', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='5569652199', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp18.save()

    emp19 = Leads(leadID='LD111666', fname='Conney', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1764097965', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp19.save()

    emp20 = Leads(leadID='LD111777', fname='Caroline', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2735005958', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp20.save()

    emp21 = Leads(leadID='LD111888', fname='Ase', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2768394890', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp21.save()

    emp22 = Leads(leadID='LD111999', fname='Florian', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1836576114', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp22.save()

    emp23 = Leads(leadID='LD222111', fname='Barbra', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='4749117151', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp23.save()

    emp24 = Leads(leadID='LD222333', fname='Koral', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='3986912324', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp24.save()

    emp25 = Leads(leadID='LD222444', fname='Sadella', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9371354173', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp25.save()

    emp26 = Leads(leadID='LD222555', fname='Johannah', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='6573158554', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp26.save()

    emp27 = Leads(leadID='LD222666', fname='Sissy', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1371568137', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp27.save()

    print("Dummy leads saved")


def addDummyLeads3():
#     This function add dummy leads

    emp1 = Leads(fname='Matilde', address='5460 Morningstar Drive', email='frew0@smh.com.au', phone='2552611487', purchaseDate='1/18/2019', pincode='346050')
    emp1.save()

    emp2 = Leads(fname='Averill', address='4 Vidon Lane', email='amather1@networkadvertising.org', phone='6094929496', purchaseDate='1/18/2019', pincode='346050')
    emp2.save()

    emp3 = Leads(fname='Rad', address='7 Badeau Parkway', email='rlidgerton2@issuu.com', phone='3501947315', purchaseDate='1/18/2019', pincode='346050')
    emp3.save()

    emp4 = Leads(fname='Chrystel', address='7 Hooker Park', email='csaunier3@livejournal.com', phone='8735251497', purchaseDate='1/18/2019', pincode='346050')
    emp4.save()

    emp5 = Leads(fname='Matilde', address='33572 Coleman Park', email='bbaudinot4@i2i.jp', phone='8388609739', purchaseDate='1/18/2019', pincode='346050')
    emp5.save()

    emp6 = Leads(fname='Barrie', address='19 Esch Center', email='mpagett5@nature.com', phone='5806994835', purchaseDate='1/18/2019', pincode='346050')
    emp6.save()

    emp7 = Leads(fname='Mercedes', address='6 Browning Lane', email='cmorilla6@dropbox.com', phone='6547662886', purchaseDate='1/18/2019', pincode='346050')
    emp7.save()

    emp8 = Leads(fname='Clemmie', address='0 Harper Crossing', email='eborghese7@goodreads.com', phone='6804954610', purchaseDate='1/18/2019', pincode='346050')
    emp8.save()

    emp9 = Leads(fname='Elmore', address='3330 Tomscot Point', email='tjills8@skype.com', phone='2739777624', purchaseDate='1/18/2019', pincode='346050')
    emp9.save()

    emp10 = Leads(fname='Tedmund', address='77 Sutteridge Crossing', email='ilagden9@friendfeed.com', phone='2658504398', purchaseDate='1/18/2019', pincode='346050')
    emp10.save()

    emp11 = Leads(fname='Iosep', address='	37 Fisk Avenue', email='ffraina@indiatimes.com', phone='3814338584', purchaseDate='1/18/2019', pincode='346050')
    emp11.save()

    emp12 = Leads(fname='Floyd', address='392 Grim Trail', email='kkilkennyb@reverbnation.com', phone='3255641713', purchaseDate='1/18/2019', pincode='346050')
    emp12.save()

    emp13 = Leads(fname='Krisha', address='65 Memorial Trail', email='ajacmardc@issuu.com', phone='2998756964', purchaseDate='1/18/2019', pincode='346050')
    emp13.save()

    emp14 = Leads(fname='Arluene', address='02852 Annamark Trail', email='atoore@feedburner.com', phone='6229489677', purchaseDate='1/18/2019', pincode='346050')
    emp14.save()

    emp15 = Leads(fname='Alexa', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='7846648659', purchaseDate='1/18/2019', pincode='346050')
    emp15.save()

    emp16 = Leads(fname='Adele', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='3922641255', purchaseDate='1/18/2019', pincode='346050')
    emp16.save()

    emp17 = Leads(fname='Jill', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2814691320', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp17.save()

    emp18 = Leads(fname='Rodie', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='5569652199', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp18.save()

    emp19 = Leads(fname='Conney', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1764097965', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp19.save()

    emp20 = Leads(fname='Caroline', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2735005958', purchaseDate='1/18/2019', pincode='346050', isContacted=True)
    emp20.save()

    emp21 = Leads(fname='Ase', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='2768394890', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp21.save()

    emp22 = Leads(fname='Florian', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1836576114', purchaseDate='1/18/2019', pincode='346050', isInterested=False, isContacted=True)
    emp22.save()

    emp23 = Leads(fname='Barbra', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='4749117151', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp23.save()

    emp24 = Leads(fname='Koral', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='3986912324', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp24.save()

    emp25 = Leads(fname='Sadella', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='9371354173', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp25.save()

    emp26 = Leads(fname='Johannah', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='6573158554', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp26.save()

    emp27 = Leads(fname='Sissy', address='8 Schurz Parkway', email='kgiraldonf@opera.com', phone='1371568137', purchaseDate='1/18/2019', pincode='346050', isInterested=True, isContacted=True)
    emp27.save()

    print("Dummy leads saved")