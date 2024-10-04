from django.db import models
from rest_framework import serializers  # type: ignore

# Create your models here.
class SysUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="使用者名稱")
    password = models.CharField(max_length=100, verbose_name="密碼")
    avatar = models.CharField(max_length=255, null=True, verbose_name="使用者頭像")
    email = models.CharField(max_length=100, null=True, verbose_name="使用者信箱")
    phonenumber = models.CharField(max_length=11, null=True, verbose_name="手機號碼")
    login_date = models.DateField(null=True, verbose_name="最後登入時間")
    status = models.IntegerField(null=True, verbose_name="帳號停用狀態")
    create_time = models.DateField(null=True, verbose_name="創建時間", )
    update_time = models.DateField(null=True, verbose_name="更新時間")
    remark = models.CharField(max_length=500, null=True, verbose_name="備註")

    class Meta:
        db_table = "sys_user"


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = '__all__'