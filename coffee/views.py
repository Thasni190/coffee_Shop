from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Coffee
# Create your views here.
def home(request):
    coffee = Coffee.objects.all()
    return render(request,'home.html',{'coffee':coffee})



def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    
    # Initialize cart in session if it doesn't exist
    cart = request.session.get('cart', {})
    
    if str(coffee_id) in cart:
        cart[str(coffee_id)] += 1
    else:
        cart[str(coffee_id)] = 1
    
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for coffee_id, quantity in cart.items():
        coffee = Coffee.objects.get(id=coffee_id)
        item_total = coffee.price * quantity
        cart_items.append({
            'coffee': coffee,
            'quantity': quantity,
            'item_total': item_total
        })
        total_price += item_total

    tax = round(total_price * 0.1, 2)  # 10% sales tax
    grand_total = round(total_price + tax, 2)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': round(total_price, 2),
        'tax': tax,
        'grand_total': grand_total
    })


def remove_from_cart(request, coffee_id):
    cart = request.session.get('cart', {})

    if str(coffee_id) in cart:
        del cart[str(coffee_id)]
        request.session['cart'] = cart

    return redirect('view_cart')
