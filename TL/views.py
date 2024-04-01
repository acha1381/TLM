from rest_framework import generics
from .models import *
from .serializers import *

class Customer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.__str__("2002")
    serializer_class = CustomerSerializer

class Order(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.__str__("2001")
    serializer_class = OrderSerializer
    
