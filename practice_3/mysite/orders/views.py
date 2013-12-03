# Create your views here.
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from orders.models import Order, Customer

class CustomersList(ListView):
	model = Order
	context_object_name = 'orders'
    
class CustomerDetails(DetailView):
	queryset = Order.objects.all()	
	context_object_name = 'order'	
