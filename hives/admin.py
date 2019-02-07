from django.contrib import admin

from .models import Hive, Breed, Pallet, Yard

admin.site.register(Hive)
admin.site.register(Breed)
admin.site.register(Pallet)
admin.site.register(Yard)

