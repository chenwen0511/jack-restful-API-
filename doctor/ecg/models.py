from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="user/%Y-%m", verbose_name="医生的头像")
    IDCard = models.CharField("用户身份证", unique=True, null=True, max_length=32)
    realName = models.CharField("用户的真实姓名", null=True, max_length=32)
    # sex = models.IntegerField("性别", choices=SEX_CHOICE, default=0)
    birtyday = models.DateField("出生年月", null=True)
    phone = models.CharField("电话", max_length=13, null=True)
    email = models.EmailField("邮箱", null=True)
    address = models.CharField("通讯地址", null=True, max_length=128)
    hospital = models.CharField("所属医院名称", null=True, max_length=64)
    hospitalID = models.IntegerField("所属医院的ID", null=True)
    department = models.CharField("所属科室名称", max_length=64, null=True)
    departemntID = models.IntegerField("所属科室ID", null=True)
    jobLevel = models.CharField("职称等级", null=True, max_length=32)
    college = models.CharField("毕业院校", null=True, max_length=64)
    personalDescription = models.TextField("个人介绍", null=True)
    remark = models.CharField("备注", max_length=128, null=True)


    def __str__(self):
        return str(self.user)

