from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    orders = Order.objects.all()
    print(request.GET)
    return render(request, 'index.html', {'orders': orders})

@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order created successfully.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'New data is not stored in the database', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Invalid Form', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form})

@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'New data is not stored in the database', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Invalid form', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form':form})

@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request, 'Order deleted successfully.', 'alert-success'))
