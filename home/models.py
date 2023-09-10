from django.db import models

# Create your models here.
# def get_path(instance, filename):
#     return f"{rollno}/{filename}"

class FilesAdmin(models.Model):
    adminupload=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)


    def __str__(self):
        return self.title

class myuploadfile(models.Model):
    STATUS1 = (
        ('2024','2024'),
        ('2025','2025'),
        ('2026','2026'),
    )
    STATUS2 = (
        ('PRML','PRML'),
        ('Software Engineering','Software Engineering'),
        ('Mathematics-1','Mathematics-1'),
        ('Mathematics-2','Mathematics-2'),
        ('Engineering-Mechanics','Engineering-Mechanics')
    )
    STATUS3 = (
        ('Tutorials','Tutorials'),
        ('Quiz','Quiz'),
        ('Major/Minor','Major/Minor'),
    )
    f_name = models.CharField(max_length=250,null = True)
    myfiles = models.FileField(upload_to='media')
    course = models.CharField(max_length=250,choices=STATUS2,null = True)
    batch  =  models.CharField(max_length=250,choices=STATUS1,null = True)
    type = models.CharField(max_length=250,choices=STATUS3,null = True)
    def __str__(self):
        return self.f_name


    




    

class Customer(models.Model):
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null = True)
   
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(max_length=200, null = True)
    category = models.CharField(max_length=200, null = True,choices=CATEGORY)
    description = models.CharField(max_length=200, null = True, blank=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    date_created = models.DateTimeField(max_length=200, null = True)
    status = models.CharField(max_length=200,null = True,choices=STATUS)
    
