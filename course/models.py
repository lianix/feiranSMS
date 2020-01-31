'''
Course information
'''

from django.db import models

from school.models import Classroom


class CourseTag(models.Model):
    name = models.CharField(max_length=32, verbose_name="类别")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "课程类别"


class Course(models.Model):
    STATUS_ITEMS = [
        (0, '预备'),
        (0, '正常'),
        (1, '结课'),
    ]
    name = models.CharField(max_length=32, verbose_name="课程名字")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="状态")
    tags = models.ManyToManyField(CourseTag, verbose_name="标签")
    classroom = models.ForeignKey(Classroom, verbose_name="教室",
        on_delete=models.SET_NULL, blank=True, null=True)

    lesson_period = models.IntegerField(default=2, verbose_name="时长")
    lesson_count = models.IntegerField(default=120, verbose_name="课时")
    lesson_week = models.IntegerField(verbose_name="上课时间")
    lesson_fee = models.IntegerField(verbose_name="课时费用")
    fee = models.IntegerField(verbose_name="课程费用")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "课程信息"


class Lesson(models.Model):
    STATUS_ITEMS = [
        (0, '取消'),
        (1, '预备'),
        (2, '上课'),
        (3, '结束'),
    ]
    times = models.PositiveIntegerField(verbose_name="课次")
    start_time = models.DateTimeField(verbose_name="上课时间")
    period = models.PositiveIntegerField(verbose_name="时长")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="状态")

    classroom = models.ForeignKey(Classroom, verbose_name="教室",
        on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)

    def __str__(self):
        return "第%d课" % self.times

    class Meta:
        verbose_name = verbose_name_plural = "课次"