from django.contrib import admin
from .models import Shirt
from .models import Pant
from .models import T_shirt
from .models import Jacket
from .models import Slides
from .models import Accessories

# Register your models here.
class ShirtAdmin(admin.ModelAdmin):
    ordering = ['Name']
    list_display = ['Name', 'Kind', 'Price',
                    'StokeSize', 'Size']

class PantAdmin(admin.ModelAdmin):
    ordering = ['Name']
    list_display = ['Name', 'Kind', 'Price',
                    'StokeSize', 'Size']

class T_shirtAdmin(admin.ModelAdmin):
    ordering = ['Name']
    list_display = ['Name', 'Kind', 'Price',
                    'StokeSize', 'Size']
class JacketAdmin(admin.ModelAdmin):
    ordering = ['Name']
    list_display = ['Name', 'Kind', 'Price',
                    'StokeSize', 'Size']

class AccessoriesAdmin(admin.ModelAdmin):
    ordering = ['Category']
    list_display = ['Category','Name','Kind','Size','StokeSize','Price']

class SlidesAdmin(admin.ModelAdmin):
    ordering = ['Title']
    list_display = ['Title', 'Comments', 'Link']

admin.site.register(Shirt,ShirtAdmin)
admin.site.register(Pant,PantAdmin)
admin.site.register(T_shirt,T_shirtAdmin)
admin.site.register(Jacket,JacketAdmin)
admin.site.register(Slides,SlidesAdmin)
admin.site.register(Accessories,AccessoriesAdmin)