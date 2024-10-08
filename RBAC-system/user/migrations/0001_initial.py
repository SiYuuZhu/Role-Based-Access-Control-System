# Generated by Django 5.1.1 on 2024-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='使用者名稱')),
                ('password', models.CharField(max_length=100, verbose_name='密碼')),
                ('avatar', models.CharField(max_length=255, null=True, verbose_name='使用者頭像')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='使用者信箱')),
                ('phonenumber', models.CharField(max_length=11, null=True, verbose_name='手機號碼')),
                ('login_date', models.DateField(null=True, verbose_name='最後登入時間')),
                ('status', models.IntegerField(null=True, verbose_name='帳號停用狀態')),
                ('create_time', models.DateField(null=True, verbose_name='創建時間')),
                ('update_time', models.DateField(null=True, verbose_name='更新時間')),
                ('remark', models.CharField(max_length=500, null=True, verbose_name='備註')),
            ],
            options={
                'db_table': 'sys_user',
            },
        ),
    ]
