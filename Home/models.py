from django.db import models

# Create your models here.
#creating class Destination
'''
class Destination:
    id: int
    Destname: str
    desc: str
    price: int
    img: str
    offer: bool
'''
#Create a table destination
class Destination(models.Model):
    Destname = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='Images')
    offer= models.BooleanField(default=False)

