from django.urls import path
from .views import (
    ShipmentListCreateView,
    ShipmentDetailView,
    ContactListCreateView,
    ContactDetailView
)

urlpatterns = [
    path('shipments/', ShipmentListCreateView.as_view(), name='shipment-list-create'),
    path('shipments/<int:pk>/', ShipmentDetailView.as_view(), name='shipment-detail'),
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]

