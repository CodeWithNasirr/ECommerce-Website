from django.db import models

# Create your models here.

class product(models.Model):
    product_id= models.AutoField
    product_name= models.CharField(max_length=50)
    category= models.CharField(max_length=50,default="")
    desc= models.CharField(max_length=300)
    price= models.IntegerField(default=0)
    pub_date= models.DateField()
    image= models.ImageField(upload_to="Shop/image",default="")

    def __str__(self):
        return self.product_name
