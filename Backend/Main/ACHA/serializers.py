from rest_framework import serializers
from .models import Shipment, Contact

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'from_location', 'to_location', 'weight', 'length', 'width', 'height', 'content']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'mobile_number', 'feedback']
