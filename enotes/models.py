from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ContactNo = models.CharField(max_length=10, null=True)
    About = models.CharField(max_length=450, null=True)
    Role = models.CharField(max_length=150, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Notes(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    ReceivedOn = models.DateField(null=True, blank=True)
    PONo = models.CharField(max_length=200, null=True)
    NameofSupplier = models.CharField(max_length=200, null=True)
    BillNo = models.CharField(max_length=200, null=True)
    BillDate = models.DateField(null=True, blank=True)
    Species = models.CharField(max_length=200, null=True)
    QtyinMT = models.CharField(max_length=200, null=True)
    BillValue = models.CharField(max_length=200, null=True)
    MIRONo = models.CharField(max_length=200, null=True)
    GivenPaymentDate = models.DateField(null=True, blank=True)
    ActualPaymentDate = models.DateField(null=True, blank=True)
    AcceptReject = models.CharField(max_length=200, null=True)
    Remark = models.CharField(max_length=450, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)
    def __str__(self):
        return self.BillNo

