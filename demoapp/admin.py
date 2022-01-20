from django.contrib import admin
from .models import Books,Contact,Student,Register
# Register your models here.

admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Books)
admin.site.register(Register)