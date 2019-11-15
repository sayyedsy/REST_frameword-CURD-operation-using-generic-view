from django.db import models

# Create your models here.
class employee(models.Model):
    empid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    salary=models.IntegerField()