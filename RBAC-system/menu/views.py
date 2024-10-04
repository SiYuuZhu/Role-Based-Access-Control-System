import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from menu.models import SysMenu, SysMenuSerializer, SysRoleMenu


# Create your views here.
class TreeListView(View):

    def buildTreeMenu(self, sysMenuList):
        resultMenuList: list[SysMenu] = list()
        for menu in sysMenuList:
            # parent
            if menu.parent_id == 0:
                resultMenuList.append(menu)
            # find its all children node
            for e in sysMenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
        return resultMenuList

    def get(self, request):
        menuQuerySet = SysMenu.objects.order_by("order_num")

        # Construct the menu tree
        sysMenuList: list[SysMenu] = self.buildTreeMenu(menuQuerySet)
        print("sysMenuList=", sysMenuList)
        serializerMenuList: list[SysMenuSerializer] = list()
        for sysMenu in sysMenuList:
            serializerMenuList.append(SysMenuSerializer(sysMenu).data)
        return JsonResponse(
            {'code': 200, 'treeList': serializerMenuList})


# OPERATIONS: GET INFO & DELETE
class ActionView(View):
    # Get menu info by ID
    def get(self, request):
        id = request.GET.get("id")
        menu_object = SysMenu.objects.get(id=id)
        return JsonResponse({'code': 200, 'menu': SysMenuSerializer(menu_object).data})

    # Delete selected Menu
    def delete(self, request):
        id = json.loads(request.body.decode("utf-8"))
        if SysMenu.objects.filter(parent_id=id).count() > 0:
            return JsonResponse({'code': 500, 'info': '請先刪除所有子選單'})
        else:
            SysRoleMenu.objects.filter(menu_id=id).delete()
            SysMenu.objects.get(id=id).delete()
            return JsonResponse({'code': 200, 'info': '該選單已成功刪除'})


# UPDATE
class SaveView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if data['id'] == -1:  # new
            obj_sysMenu = SysMenu(name=data['name'], icon=data['icon'],
                                  parent_id=data['parent_id'], order_num=data['order_num'], path=data['path'],
                                  component=data['component'], menu_type=data['menu_type'], perms=data['perms'],
                                  remark=data['remark'])
            obj_sysMenu.create_time = datetime.now().date()
            obj_sysMenu.save()
        else:                 # save for change
            obj_sysMenu = SysMenu(id=data['id'], name=data['name'], icon=data['icon'],
                                  parent_id=data['parent_id'], order_num=data['order_num'], path=data['path'],
                                  component=data['component'], menu_type=data['menu_type'], perms=data['perms'],
                                  remark=data['remark'], create_time=data['create_time'],
                                  update_time=data['update_time'])
            obj_sysMenu.update_time = datetime.now().date()
            obj_sysMenu.save()
        return JsonResponse({'code': 200, 'info':'選單更新成功'})
