from django.db import models
from rest_framework import serializers
from role.models import SysRole


# Menu
class SysMenu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True,verbose_name="選單名稱")
    icon = models.CharField(max_length=100,null=True,verbose_name="選單圖示")
    parent_id = models.IntegerField(null=True,verbose_name="父選單ID")
    order_num = models.IntegerField(null=True,verbose_name="顯示順序")
    path = models.CharField(max_length=200,null=True,verbose_name="路由地址")
    component =models.CharField(max_length=255,null=True,verbose_name="組件路徑")
    menu_type =models.CharField(max_length=1,null=True,verbose_name="選單類型 - M目錄 C選單 F按鈕")
    perms = models.CharField(max_length=100,null=True,verbose_name="權限標識")
    create_time = models.DateField(null=True,verbose_name="創建時間",)
    update_time = models.DateField(null=True,verbose_name="更新時間")
    remark = models.CharField(max_length=500,null=True,verbose_name="備註")

    def __lt__(self,other):
        return self.order_num < other.order_num
    
    class Meta:
        db_table = "sys_menu"


class SysMenuSerializer(serializers.ModelSerializer):
    children=serializers.SerializerMethodField()

    def get_children(self,obj):
        print("menu serializer: children")
        if hasattr(obj, "children"):
            serializerMenuList: list[SysMenuSerializer2] = list()
            for sysMenu in obj.children:
                serializerMenuList.append(SysMenuSerializer2(sysMenu).data)
            return serializerMenuList
        
    class Meta:
        model=SysMenu
        fields='__all__'


class SysMenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model=SysMenu
        fields='__all__'


# Role <-> Menu
class SysRoleMenu(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole,on_delete=models.PROTECT)
    menu = models.ForeignKey(SysMenu,on_delete=models.PROTECT)

    class Meta:
        db_table = "sys_role_menu"


class SysRoleMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRoleMenu
        fields = '__all__'