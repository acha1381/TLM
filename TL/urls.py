from django.urls import path
from .views import *

urlpatterns = [ 
    path('Customer/',Customer.as_view(), name="Customer"),
    path("<int:pk>", CustomerDetail.as_view(), name="Cust")
    
]

urlpatterns = [ 
    path('Order/',Order.as_view(), name="Customer"),
    path("<int:pk>", OrderDetail.as_view(), name="Cust")
    
]