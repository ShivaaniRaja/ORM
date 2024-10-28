# Ex02 Django ORM Web Application
## Date: 28.10.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-28 094226.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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


admin.py
from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)


```


## OUTPUT

![alt text](<Screenshot 2024-10-28 092704.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
