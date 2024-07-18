from django.contrib import admin

from.models import student 

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'Name', 'Email']

admin.site.register(student,StudentAdmin)