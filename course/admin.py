from django.contrib import admin

from .models import CourseTag, Course, Lesson

admin.site.register(CourseTag)
admin.site.register(Course)
admin.site.register(Lesson)
