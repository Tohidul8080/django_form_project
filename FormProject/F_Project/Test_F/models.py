from django.db import models

# Create your models here.
class F_table(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    id_number=models.IntegerField()
    cgpa=models.FloatField()

    def __str__(self) :
        return self.first_name+ " "+ self.last_name
    
    