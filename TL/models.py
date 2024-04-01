from django.db import models

# Create your models here.
class Customer(models.Model):
    Customer_Id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    Ph_no=models.IntegerField(max_length=15)
    email=models.EmailField()


    def __str__(self):
        return str(self.Customer_Id)

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderStatus = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.OrderID)

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    QuantityAvailable = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.ProductID)

class OrderProduct(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('OrderID', 'ProductID'),)

class Vehicle(models.Model):
    VehicleID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=50)
    Capacity = models.DecimalField(max_digits=10, decimal_places=2)
    AvailabilityStatus = models.BooleanField(default=False)

    def __str__(self):
        return str(self.AvailabilityStatus)

class Route(models.Model):
    RouteID = models.AutoField(primary_key=True)
    Origin = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Distance = models.DecimalField(max_digits=10, decimal_places=2)
    EstimatedTravelTime = models.TimeField()

    def __str__(self):
        return str(self.Destination)

class VehicleRoute(models.Model):
    VehicleID = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('VehicleID', 'RouteID'),)

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Role = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=15)
    Email = models.EmailField()

    def __str__(self):
        return str(self.ContactNumber)

class OrderEmployee(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('OrderID', 'EmployeeID'),)
