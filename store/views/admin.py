from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth import authenticate
from django.views import  View
from requests import request
from store.models import product

from store.models.category import Category
from store.models.product import Product


class Admin(View):
    return_url = None
    def get(self , request):
        Admin.return_url = request.GET.get('return_url')
        return render(request , 'admin.html')

    def post(self , request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        admin=authenticate(username=username,password=password)
        error_message = None
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['admin'] =admin
        if admin:
            request.session['admin'] = admin.id
            print("admin_id",admin.id)
            if Admin.return_url:
                    return HttpResponseRedirect(Admin.return_url)
            else:
                Admin.return_url = None
                print(products)
                return render(request,'index.html',{'products':products,'admin':admin})
        else:
            error_message = 'Username or Password invalid !!'
        
        return render(request, 'admin.html', {'error': error_message})

def Admin_logout(request):
    request.session.clear()
    return redirect('home')


def Edit(request):
    print("Entered")
    product=Product.objects.get(pk=request.POST.get('product'))
    return render(request,'edit.html',{'product':product})
