from django.db import models



class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()

    def __str__(self):
        return f'Shipment {self.id} from {self.from_location} to {self.to_location}'

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    feedback = models.TextField()

    def __str__(self):
        return self.name
