from django.db import models

# Create your models here.

class Person(models.Model):

    pfirst_name = models.CharField(max_length=50)
    plast_name = models.CharField(max_length=50)
    pphone_number = models.CharField(max_length=50)
    pemail = models.EmailField()

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.pfirst_name +" "+ self.plast_name +" "+ self.pphone_number +" "+ self.pemail
