from django.contrib import admin

from .models import Student, Mycourse, Mylesson

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'age', 'created_time')
    list_filter = ('sex', 'age', 'created_time')
    search_fileds = ('name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Mycourse)
admin.site.register(Mylesson)