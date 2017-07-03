from django.contrib import admin
from mobapp.models import product
from mobapp.models import Brands
from mobapp.models import pro_brand_map
from mobapp.models import Pro_models
from mobapp.models import Rating
from mobapp.models import booking
# Register your models here.

admin.site.register(product)
admin.site.register(Brands)
admin.site.register(pro_brand_map)
admin.site.register(Pro_models)
admin.site.register(Rating)
admin.site.register(booking)
