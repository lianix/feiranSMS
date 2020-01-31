from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "标签信息"


class School(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "学校信息"


class Classroom(models.Model):
    STATUS_ITEMS = [
        (0, '正常'),
        (1, '维修'),
    ]
    name = models.CharField(max_length=32, verbose_name="姓名")
    capacity = models.IntegerField(verbose_name= "容量")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="状态")
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    school = models.ForeignKey(School, verbose_name='学校',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "教室信息"


# Human information
class Human(models.Model):
    SEX_ITEMS = [
        (0, "未知"),
        (1, "男"),
        (2, "女"),
    ]
    name = models.CharField(max_length=32, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name= "性别", blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name= "年龄", blank=True, null=True)
    birthday = models.DateField(verbose_name= "生日", blank=True, null=True)
    phone = models.CharField(max_length=32, verbose_name="手机", blank=True, null=True)
    wechat = models.CharField(max_length=128, verbose_name="微信", blank=True, null=True)
    qq = models.CharField(max_length=128, verbose_name="QQ", blank=True, null=True)
    email = models.EmailField(verbose_name="邮箱", blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False,
        verbose_name="创建时间")

    class Meta:
        abstract = True


class Role(models.Model):
    title = models.CharField(max_length=32,verbose_name='职位')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "职位"


class Staff(Human):
    salary = models.IntegerField(verbose_name='工资', blank=True, null=True)
    graduated = models.CharField(max_length=32, verbose_name="毕业院校", blank=True, null=True)
    title = models.ForeignKey(Role, verbose_name='职位',
        on_delete=models.SET_NULL, blank=True, null=True)
    school = models.ForeignKey(School, verbose_name='学校',
        on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "员工信息"
