from django.contrib import admin
from .modelss import StudentClasses, Student, Classes

# Register your models here.
@admin.register(StudentClasses)
class TCAdmin(admin.ModelAdmin):
    list_display = ['student','name', 'date_from', 'date_to'] # To change the displayed option in the listed items
    list_filter = ['name']
    search_fields = ['name' , 'date_from', 'date_to']

admin.site.register(Student) # Add  a new Model --> model = table
admin.site.register(Classes) # Add  a new Model --> model = table


