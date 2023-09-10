from django.contrib import admin
from .models import FilesAdmin,myuploadfile,Customer
from .models import Product,Order
from .models import Tag
# Register your models here.
admin.site.register(FilesAdmin)
admin.site.register(myuploadfile)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
