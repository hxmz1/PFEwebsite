from django.contrib.gis import admin
from .models import *
# Register your models here.
admin.site.register(Superviseur)
admin.site.register(Client)
admin.site.register(Data)
admin.site.register(nodes)


