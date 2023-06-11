from django.contrib import admin

from application1.models import Registerdata
class Registeradmin(admin.ModelAdmin):
    list_display=['rollno','name','dep','gender']

admin.site.register(Registerdata,Registeradmin)
