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
    id = models.IntegerField(primary_key=True)
    Ico = models.ImageField()
    Name = models.CharField(max_length=30, null=True)
    Soname = models.CharField(max_length=30, null=True)
    Phone = models.CharField(max_length=30, null=True)
    Email = models.EmailField(max_length=40, null=False)
    IsActive = models.BooleanField(null=True)
    LastActive = models.DateTimeField(auto_now = True)
    DateOfRegistration = models.DateTimeField(auto_now_add = True)
    PresentCode = models.CharField(max_length=30, null=True)
    UserBalance = models.ForeignKey('Balance', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.Name)

class Balance(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30, null=True)
    Soname = models.CharField(max_length=30, null=True)
    DateOfCreation = models.DateTimeField(auto_now_add = True)
    Bonuses = models.IntegerField(null=True)
    Money = models.IntegerField(null=True)
    TypeOperation = models.CharField(max_length=10, null=True)
    Status = models.CharField(max_length=10, null=True)
    DateOfOperation = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return str(self.DateOfCreation, self.Bonuses, self.Money, self.TypeOperation, self.Status, self.DateOfOperation)
