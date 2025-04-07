from django.contrib import admin
from app.models import Faculty,student,Employee,user_data
# Register your models here.
admin.site.register(student)
admin.site.register(Faculty)
admin.site.register(Employee)
admin.site.register(user_data)