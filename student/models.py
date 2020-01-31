from django.db import models

from school.models import Human
from course.models import Course, Lesson


class Student(Human):
    STATUS_ITEMS = [
        (0, '预备学员'),
        (1, '试听学员'),
        (2, '在读学员'),
        (3, '结课学员'),
        (4, '退费学员'),
    ]

    total_tuition = models.IntegerField(verbose_name= "学费", editable=False, blank=True, null=True)
    total_remained = models.IntegerField(verbose_name= "剩余学费", editable=False, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"


class Mycourse(models.Model):
    name = models.CharField(max_length=32, verbose_name="我的课程")
    tuition = models.IntegerField(verbose_name= "学费")
    remained = models.IntegerField(verbose_name= "剩余学费")

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cource = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "我的课程"


class Mylesson(models.Model):
    STATUS_ITEMS = [
        (0, '上课'),
        (1, '请假'),
        (2, '调课'),
    ]
    name = models.CharField(max_length=32, verbose_name="我的课次")
    cource = models.ForeignKey(Mycourse, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "我的课次"