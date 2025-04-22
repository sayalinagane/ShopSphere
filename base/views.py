from django.shortcuts import render,redirect
from.models import Products,CartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CheckoutForm
from .models import CartModel
from .forms import ContactForm
from django.contrib import messages



# Create your views here.
def home(request):
    trend=False
    offer=False

    # count_=CartModel.objects.filter(host=request.user).count()     
    # print(count_)

    all_products=Products.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        print(q)
        all_products=Products.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q)|Q(category__icontains=q)) 
        messages.add_message(request,messages.WARNING,'no match found')

               
    if 't' in request.GET:
        trend=True
        all_products=Products.objects.filter(trending=1)

    if 'offer' in request.GET:
        offer=True
        all_products=Products.objects.filter(offer=1)
    
    if 'cat_form' in request.GET:
        cat_form = request.GET['cat_form']
        print(cat_form.lower())
        all_products=Products.objects.filter(category=cat_form.lower())

    cat=[]
    for i in all_products:
        print(i.category)
        if i.category not in cat:
            cat+=[i.category]
    print(cat)


    # if request.method == 'POST':
    #     category=request.POST['category']
    #     name=request.POST['name']
    #     desc=request.POST['desc']
    #     price=request.POST['price']
    #     pimg=request.FILES['pimg']
    #     Products.objects.create(category=category,name=name,desc=desc,price=price,p_images=pimg)
    #     print(category,name,desc,price,pimg)

    return render(request,'home.html',{'all_products':all_products,'trend':trend,'offer':offer,'cat':cat})

@login_required(login_url='login_')
def cart(request):
    cart_nav=True
    cart_data=CartModel.objects.filter(host=request.user)
    
    Totalpay=0
    for i in cart_data:
        Totalpay+=i.totalamount  
    
    messages.add_message(request,messages.SUCCESS,'login successfully done !! welcome to shopsphere')

    return render(request,'cart.html',{"cart_nav":cart_nav,'cart_data':cart_data,'Totalpay':Totalpay})

@login_required(login_url='login_')
def addtocart(request,pk):

    Product=Products.objects.get(id=pk)

    try:
        Cart_item=CartModel.objects.get(name=Product.name,host=request.user)
        Cart_item.quantity+=1
        Cart_item.totalamount+=Product.price
        Cart_item.save()
        return redirect('cart')

    except:
        CartModel.objects.create(
        category=Product.category,
        name=Product.name,
        desc=Product.desc,
        price=Product.price,
        totalamount=Product.price,
        host=request.user


    )

    return redirect('cart')


# def show_total_amount(request):
#     cart_nav=True
#     cart_data = CartModel.objects.all()
#     total_amount = 0
#     for item in cart_data:
#         total_amount += item.totalamount

#     return render(request, 'cart.html', {
#         'cart_data': cart_data,
#         'cart_nav': cart_nav,
#         'total_amount': total_amount
#     })

@login_required(login_url='login_')
def remove_from_cart(request, id):
     item = CartModel.objects.get(id=id)
     item.delete()
     return redirect('cart')

def support(request):
    return render(request,'support.html')


def checkout(request):
    cart_data = CartModel.objects.filter(host=request.user)
    total_amount = 0
    for item in cart_data:
        total_amount += item.totalamount

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            # optionally clear cart or redirect
            return render(request, 'cart.html')
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {
        'form': form,
        'cart_data': cart_data,
        'total_amount': total_amount
    })


def product_details(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'product_details.html', {'product': product})

def support(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Redirect to the same page or a success page
    else:
        form = ContactForm()

    return render(request, 'support.html', {'form': form})