from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import orderdata, orderdata1, orderdata2
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def index(request):
  return render(request,'index.html')

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def product(request):
  template = loader.get_template('product.html')
  return HttpResponse(template.render())

def testimonial(request):
  template = loader.get_template('testimonial.html')
  return HttpResponse(template.render())

def service(request):
  template = loader.get_template('service.html')
  return HttpResponse(template.render())

def order(request):
  mydata=orderdata.objects.all()
  if(mydata!=""):
    return render(request,'order.html',{"datas":mydata})
  else:
    return render(request,'order.html')    
      
    

def addData(request):
    if request.method =='POST':
        flavour=request.POST['flavour']
        weight=request.POST['weight']
        quantity=request.POST['quantity']
        price=request.POST['price']
        discount=request.POST['discount']
        disprice=request.POST['disprice']
        address=request.POST['address']
        pincode=request.POST['pincode']
        mobile=request.POST['mobile']
        
        obj=orderdata()
        obj.Flavour=flavour
        obj.Weight=weight
        obj.Quantity=quantity
        obj.Actual_Price=price
        obj.Discount=discount
        obj.Discount_Price=disprice
        obj.Delivery_Address=address
        obj.Pincode=pincode
        obj.Mobile=mobile
        obj.save()
        messages.success(request,("Order Placed Successful!"))
        
        mydata=orderdata.objects.all()
        return redirect('order')
    return render(request,'order.html')

def order1(request):
  mydata=orderdata1.objects.all()
  if(mydata!=""):
    return render(request,'order1.html',{"datas":mydata})
  else:
    return render(request,'order1.html')    
      
    

def addData1(request):
    if request.method =='POST':
        flavour1=request.POST['flavour1']
        weight1=request.POST['weight1']
        quantity1=request.POST['quantity1']
        price1=request.POST['price1']
        discount1=request.POST['discount1']
        disprice1=request.POST['disprice1']
        address1=request.POST['address1']
        pincode1=request.POST['pincode1']
        mobile1=request.POST['mobile1']
        
        obj=orderdata1()
        obj.Flavour=flavour1
        obj.Weight=weight1
        obj.Quantity=quantity1
        obj.Actual_Price=price1
        obj.Discount=discount1
        obj.Discount_Price=disprice1
        obj.Delivery_Address=address1
        obj.Pincode=pincode1
        obj.Mobile=mobile1
        obj.save()
        messages.success(request,("Order Placed Successful!"))
        
        mydata=orderdata1.objects.all()
        return redirect('order1')
    return render(request,'order1.html')

def order2(request):
  mydata=orderdata2.objects.all()
  if(mydata!=""):
    return render(request,'order2.html',{"datas":mydata})
  else:
    return render(request,'order2.html')    
      
    

def addData2(request):
    if request.method =='POST':
        flavour2=request.POST['flavour2']
        weight2=request.POST['weight2']
        quantity2=request.POST['quantity2']
        price2=request.POST['price2']
        discount2=request.POST['discount2']
        disprice2=request.POST['disprice2']
        address2=request.POST['address2']
        pincode2=request.POST['pincode2']
        mobile2=request.POST['mobile2']
        
        obj=orderdata2()
        obj.Flavour=flavour2
        obj.Weight=weight2
        obj.Quantity=quantity2
        obj.Actual_Price=price2
        obj.Discount=discount2
        obj.Discount_Price=disprice2
        obj.Delivery_Address=address2
        obj.Pincode=pincode2
        obj.Mobile=mobile2
        obj.save()
        messages.success(request,("Order Placed Successful!"))
        
        mydata=orderdata2.objects.all()
        return redirect('order2')
    return render(request,'order2.html')

def signin(request):
  
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('index')
      else:
        messages.success(request, ("There was an Error Logging In, Try Again..."))
        return redirect('signin')
    else:  
      return render(request,'signin.html', {}) 
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('index')

def details(request):
    if request.method == 'POST':
      form = RegisterUserForm(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, ("Registration Successful!"))
        return redirect('signin')
    else:
      form = RegisterUserForm()
      return render(request,'details.html', {'form':form})
