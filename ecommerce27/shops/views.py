from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, Category


# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    return render(request,'home.html',{'products':products})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1 = request.POST['password1']
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request, user)
            full_name=user.get_full_name() or user.username
            return render(request,'user_dashboard.html',{'full_name': full_name})
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

def add_product(request):
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request,"Successfully added new product")
    product_form=ProductForm()
    return render(request, 'add_products.html',{'form':product_form})

def edit_product(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES,instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Successfully added the product")
    product_form=ProductForm(instance=product)
    return render(request, 'edit_product.html',{'form':product_form})

def delete_product(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request,'delete_product.html',{'product':product})

def user_dashboard(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'category': category})

def search(request, products=None):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )
        return render(request,'home.html',{'products':products})
    else:
        results = Product.objects.none()

    return render(request, 'search_results.html', {'products': products, 'query': query})

def contact_us(request):
    return render(request,'contact_us.html')

