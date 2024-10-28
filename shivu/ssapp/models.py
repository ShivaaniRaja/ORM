
from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
   cid=models.CharField(max_length=20,primary_key="bid")
   name=models.CharField(max_length=100)
   amount=models.IntegerField()
   interest=models.IntegerField()
   email=models.EmailField()


class BankLoanAdmin(admin.ModelAdmin):
   list_display=('cid','name','amount','interest','email')


