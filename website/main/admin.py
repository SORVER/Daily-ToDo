from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Day)
admin.site.register(Task)
admin.site.register(DefaultDay)
admin.site.register(DefaultTask)