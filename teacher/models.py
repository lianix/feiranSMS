from django.db import models

from school.models import Human

class Teacher(Human):
    TYPE_ITEMS = [
        (0, '临时教师'),
        (1, '兼职教师'),
        (2, '全职教师'),
    ]
    STATUS_ITEMS = [
        (0, '待考核'),
        (1, '正常'),
        (2, '休假'),
    ]

    kind = models.IntegerField(choices=TYPE_ITEMS, default=0, verbose_name="类型")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "教师信息"