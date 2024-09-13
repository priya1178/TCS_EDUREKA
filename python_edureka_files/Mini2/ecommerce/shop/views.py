from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from django.core.mail import send_mail  # Import if you plan to send emails


@login_required
def add_to_cart(request, product_id):
    # Ensure `Product` is used, not a function or other incorrect reference
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('products')  # Ensure 'products' is a valid URL name

@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    
    # Calculate total price
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    
    return render(request, 'shop/cart.html', {'cart': cart, 'total_price': total_price})

'''
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        # Add the product to the cart
        # Implement cart logic here
        # For example, you might store cart data in the session or a database
        # Here we'll simply redirect to the products page
        return redirect('product_list')
    return redirect('product_list')
'''

def homepage(request):
    return render(request, 'shop/homepage.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"Received message from {name} ({email}): {message}")

            # Example: Send an email (optional)
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=['your-email@example.com'],  # Replace with your email
            )

            # Redirect to success page
            return redirect('contact_us_success')
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
            return render(request, 'shop/contact_us.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'shop/contact_us.html', {'form': form})
    
def contact_us_success(request):
    return render(request, 'shop/contact_us_success.html')

    return render(request, 'shop/contact_us.html', {'form': form})

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'shop/product_list.html', {'products': products})
