# Create your models here.
from django.db import models
from django.forms import ModelForm


class DataSetDesc(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    environment_type = models.CharField(
        max_length=4,
        choices=[
            ('DEV',"Development"),
            ('PROD',"Production"),
            ('UAT',"Staging")            
        ]
    )
    dataid = models.IntegerField()

    def json(self):
        return {
            "name": self.name,
            "desc" : self.desc,
            "environment_type" : self.environment_type,
            "dataid" : self.dataid,
        }

class DataSetDescForm(ModelForm):
    class Meta:
        model = DataSetDesc
        fields = ['name','environment_type']
 
class Trade(models.Model):
    tradeid = models.IntegerField()
    orderid = models.IntegerField()
    ticker = models.CharField(max_length=256)
    environment_type = models.CharField(
        max_length=4,
        choices=[
            ('DEV',"Development"),
            ('PROD',"Production"),
            ('UAT',"Staging")            
        ]
    )
    price = models.FloatField()
    size = models.IntegerField()

class Order(models.Model):
    orderid = models.IntegerField()
    ticker = models.CharField(max_length=256)
    environment_type = models.CharField(
        max_length=4,
        choices=[
            ('DEV',"Development"),
            ('PROD',"Production"),
            ('UAT',"Staging")            
        ]
    )
    price = models.FloatField()
    size = models.IntegerField()
    state   = models.CharField(
        max_length=4,
        choices=[
            ('O',"Open"),
            ('E',"Executed"),
            ('P',"Partial"),
            ('C',"Cancelled")           
        ]
    )