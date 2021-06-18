from django.db import models

class Transport(models.Model):
    Qr_code = models.IntegerField(null=False, unique = True)
    Serial_number = models.IntegerField(null=False, unique = True)
    Battery = models.IntegerField(null=False)
    Price = models.CharField(max_length = 30, null=True)
    Power = models.CharField(max_length = 30)
    Trip = models.IntegerField(null=True)
    Status = models.CharField(max_length = 30,null=True)
    Action = models.BooleanField(null=True)
    def __str__(self):
        return str(self.Qr_code)

class User(models.Model):
    Ico = models.ImageField()
    Name = models.CharField(max_length=30, null=True)
    Soname = models.CharField(max_length=30, null=True)
    Phone = models.CharField(max_length=30, null=True)
    Email = models.EmailField(max_length=40, null=False)
    IsActive = models.BooleanField()
    LastActive = models.DateTimeField()
    DateOfRegistration = models.DateTimeField()
    PresentCode = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.Name)
