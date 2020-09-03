from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    role=models.CharField(max_length=100)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(null=True,blank=True)
    image=models.ImageField(upload_to='images/')

def _dtr_(self):
    return self.title+"-"+self.role