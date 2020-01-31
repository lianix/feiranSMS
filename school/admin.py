from django.contrib import admin

from .models import School, Classroom, Staff, Tag, Role

admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Staff)
admin.site.register(Tag)
admin.site.register(Role)