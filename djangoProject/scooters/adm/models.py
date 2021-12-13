from django.db import models
from django.urls import reverse


class Transport(models.Model):
    Qr_code = models.IntegerField(null=False, unique=True)
    Serial_number = models.IntegerField(null=False, unique=True)
    Battery = models.IntegerField(null=False)
    Price = models.CharField(max_length=30, null=True)
    Power = models.CharField(max_length=30)
    Trip = models.IntegerField(null=True)
    Status = models.CharField(max_length=30, null=True)
    Action = models.BooleanField(null=True)
    def __str__(self):
        return str(self.Qr_code)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    Ico = models.ImageField()
    Name = models.CharField(max_length=30, null=True)
    Soname = models.CharField(max_length=30, null=True)
    Phone = models.CharField(max_length=30, null=True)
    Email = models.EmailField(max_length=40, null=False)
    IsActive = models.BooleanField(null=True)
    LastActive = models.DateTimeField(auto_now=True)
    DateOfRegistration = models.DateTimeField(auto_now_add=True)
    PresentCode = models.CharField(max_length=30, null=True)
    UserBalance = models.ForeignKey('Balance', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.Name)
    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})

class Balance(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30, null=True)
    Soname = models.CharField(max_length=30, null=True)
    DateOfCreation = models.DateTimeField(auto_now_add=True)
    Bonuses = models.IntegerField(null=True)
    Money = models.IntegerField(null=True)
    TypeOperation = models.CharField(max_length=10, null=True)
    Status = models.CharField(max_length=10, null=True)
    DateOfOperation = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.DateOfCreation, self.Bonuses, self.Money, self.TypeOperation, self.Status, self.DateOfOperation)

class TypeOfZone(models.Model):
    TypeZone = models.CharField(max_length=30, null=True)
    ColorZone = models.CharField(max_length=7, null=True)
    CanYouScooterOnThisArea = models.BooleanField(null=True)
    CanYouParkingOnThisArea = models.BooleanField(null=True)
    MaxSpeed = models.IntegerField(null=True, max_length=3)
    Description = models.CharField(max_length=50, null=True)
    def __str__(self):
        return str(self.TypeZone)

class Zone(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30, null=True)
    TypeZone = models.ForeignKey(TypeOfZone, on_delete=models.SET_NULL, null=True)
    GPSPoints = models.TextField()
    ColorZone =  models.CharField(max_length=7)
    def __str__(self):
        return str(self.Name)

    def get_absolute_url(self):
        return reverse('zoneredactor', kwargs={'pk': self.pk})

class TypesOfPromoCodes(models.Model):
    TypeOfPromoCode = models.CharField(max_length=30, null=True)
    def __str__(self):
        return str(self.TypeOfPromoCode)

class StatusesOfPromoCodes(models.Model):
    StatusOfPromoCode = models.CharField(max_length=30, null=True)
    def __str__(self):
        return str(self.StatusOfPromoCode)

class PromoCodes(models.Model):
    NameOfPromoCode = models.CharField(max_length=30, null=True)
    TypeOfPromoCode = models.ForeignKey(TypesOfPromoCodes, on_delete=models.SET_NULL, null=True)
    StatusOfPromoCode = models.ForeignKey(StatusesOfPromoCodes, on_delete=models.SET_NULL, null=True)
    Limit = models.IntegerField(null=True, max_length=3)
    Sum = models.DecimalField(max_digits=7, decimal_places=2)
    StartOfActive = models.DateTimeField(auto_now=False, auto_now_add=False)
    EndOfActive = models.DateTimeField(auto_now=False, auto_now_add=False)
    DateOfCreation = models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return str(self.NameOfPromoCode)


