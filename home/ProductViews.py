from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .views import success,fail
from django.shortcuts import HttpResponseRedirect

import pyqrcode



#USED IN ADMIN SIDE FOR CREATING AND MANAGING NEW PRODUCT FOR INVENTORY
@csrf_exempt
def createNewDevice(request):
    folder="ProductImages"
    if request.method=="POST":
        name=request.POST.get("name",None)
        year=request.POST.get("year",None)
        product_id=request.POST.get("id",None)
        cost=request.POST.get("cost",None)
        description=request.POST.get("description",None)
        category=request.POST.get("cat",None)
        feature=request.POST.get("feature",None)
        image=request.FILES.get("pimage",None)
        print(request.POST)


        if (not(name==None and year==None and product_id==None and cost==None and description==None and category==None and feature==None)):
            print (name)
            print(year)
            print(category)
            print("thats all")
            try:
                fs = FileSystemStorage(location=folder)  # defaults to   MEDIA_ROOT
                filename = fs.save(image.name, image)
                file_url = fs.url(filename)
                print(file_url)
                newProduct=Product(name=name,year=year,product_id=product_id,cost=cost,description=description,category=category,features=feature,image_path=file_url)
                newProduct.save()
                print(newProduct.id)
                qr=pyqrcode.create(product_id)
                qr.svg('home/static/qrcode/'+product_id+".svg",scale=8)
                out={}
                out['id']=product_id
                return success(out)
            except Product.DoesNotExist:
                return fail("PID exist")

        else:
            return fail("Invalid credentials")

    return fail("something went wrong")


@csrf_exempt
def displayAllDevice(request):
    print("***********hjjjh********")
    products=Product.objects.all()
    out=[]
    for i in range(len(products)):
        pro=products[i]
        product={}
        product['id']=pro.id;
        product['name']=pro.name
        product['year']=pro.year
        product['product_id']=pro.product_id
        product['cost']=pro.cost
        product['description']=pro.description
        product['feature']=pro.features
        product['category']=pro.category
        out.append(product)

    return success(out)


@csrf_exempt
def deleteDevice(request):
    if request.method=="POST":
        product_id=request.POST.get("product_id",None)
        if(not(product_id==None)):
            try:
                product=Product.objects.get(product_id=product_id)
                product.delete()
                return success("Item deleted")
            except:
                return fail("Product id does not exist")
        else:
            return fail("fail")

@csrf_exempt
@csrf_exempt
def editProduct(request):
    if request.method=="POST":
        id=request.POST.get("id",None)
        name=request.POST.get("name",None)
        year = request.POST.get("year", None)
        product_id = request.POST.get("product_id", None)
        cost = request.POST.get("cost", None)
        description = request.POST.get("description", None)
        category = request.POST.get("category", None)
        feature = request.POST.get("feature", None)
        if (not (name == None or year == None or product_id == None or cost == None or description == None or category == None or feature == None)):
            print(name)
            print(year)
            print(category)
            print("thats all")
            try:
                product=Product.objects.get(id=id)
                product.name=name
                product.product_id=product_id
                product.year=year
                product.category=category
                product.description=description
                product.cost=cost
                product.features=feature
                product.save()
                return success("Products available")

            except:
                return fail("Product id already exists")

        else:
            return fail("Invalid credentials")

#-------------------------------------------------------------------------------------------------#


#3 apis

@csrf_exempt
def addNewProductToInventory(request):
    if(request.method=="POST"):
        location=request.POST.get("location",None)
        product_id=request.POST.get("product_id",None)
        qty=request.POST.get("qty",None)
        if(location==None or product_id==None or qty==None):
            return fail("Invalid value")
        else:
            try:
                product=Product.objects.get(product_id=product_id)
                inventory_obj=Inventory.objects.get(product=product,goDown=location)
                inventory_obj.qty=qty
                inventory_obj.save()
                return success('new object added')
            except Product.DoesNotExist:
                return fail("product does not exists")
            except Inventory.DoesNotExist:
                #item does not exist in inventory so add a new item
                inventory_obj=Inventory(product=product,goDown=location,qty=qty)
                inventory_obj.save()
                return success("New object added")

@csrf_exempt
def displayAllProducts(request):
    if(request.method=="POST"):
        print("post came in")
        location = request.POST.get("location", None)
        if(location==None):
            return fail("no value")
        else:
            inventory_obj=Inventory.objects.filter(goDown=location)
            out=[]
            for inventory in inventory_obj:
                invent={}
                invent['id']=inventory.product.product_id
                invent['qty']=inventory.qty
                invent['name']=inventory.product.name
                invent['type']=inventory.product.category
                out.append(invent)
            return success(out)


    return fail("Invalid value")

@csrf_exempt
def editProductQty(request):
    if(request.method=="POST"):
        product_id=request.POST.get("product_id",None)
        location=request.POST.get("location",None)
        qty=request.POST.get("qty",None)
        if(product_id==None or location==None):
            return fail("Invalid data")
        else:
            try:
                product=Product.objects.get(product_id=product_id)
                inventory=Inventory.objects.get(product=product,goDown=location)
                inventory.qty=qty
                inventory.save()
                return success("qantity updated")
            except Product.DoesNotExist:
                return fail("invalid product")

#only for the single product
@csrf_exempt
def singleProductQty(request):
    if(request.method=="POST"):
        product_id=request.POST.get("product_id",None)
        branch=request.POST.get("branch",None)
        if(product_id==None or branch==None):
            return fail("Invalid data");
        else:
            inventory=Inventory.objects.get(product_id=product_id,goDown=branch)
            if inventory is not None:
                single_produt={}
                single_produt['id']=inventory.id
                single_produt['qty']=str(inventory.qty)
                single_produt['branch']=inventory.goDown
                single_produt['product']=inventory.product.name
                return success(single_produt)

#adding stock from the app not from the web                
@csrf_exempt
def addStock(request):
    if(request.method=="POST"):
        product_id=request.POST.get("product_id",None)
        branch=request.POST.get("branch",None)
        qty=request.POST.get("qty",None)
        print(qty)
        if(product_id==None or branch==None or qty==None):
            return fail("invaid data")
        else:
            inventory=Inventory.objects.get(product_id=product_id,goDown=branch)
            if inventory is not None:
                inventory.qty=inventory.qty+int(qty)
                
                inventory.save()
                return success("product qunatityt is added")
            else:
                return fail("product or branch not found")

    else:
        return fail("invalid data")

#existing qunatity will be given to the technician and decreased in the branch
@csrf_exempt
def removeStock(request):
    if(request.method=="POST"):
        qty=request.POST.get("qty")
        branch=request.POST.get("branch")
        tech_id=request.POST.get("tech_id")
        product_id=request.POST.get("product_id")
        product=Product.objects.get(id=product_id)
        tech=Employee.objects.get(id=tech_id)
        if product is not None and tech is not None:
            inventory=Inventory.objects.get(product=product)
            if inventory is not None:
                if(inventory.qty < int(qty)):
                    return fail("sorry expected qunatity cannot be given")

                else:

                    inventory.qty=inventory.qty - int(qty)
                    inventory.save()
                    Tech=TechnicianStock(product=product,technician=tech,qty=qty,branch=branch)
                    Tech.save()
                    endres=qty+" "+product.name+" handed over to the technician"
                    return success(endres)


            else:
                return fail("product not found in inventory")
            
        else:
            return fail("invalid data")


    else:
        return fail("Invalid data");