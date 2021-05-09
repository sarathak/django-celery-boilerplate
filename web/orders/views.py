from django.http import HttpResponse
from django.shortcuts import render
from orders.forms import OrderForm
from orders.tasks import create_order


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            products = form.cleaned_data.get('products')
            price = form.cleaned_data.get('price')
            create_order.delay(products,price)
            return HttpResponse('Order created')
    else:
        form = OrderForm()
    return render(request, 'index.html', {'form': form})
