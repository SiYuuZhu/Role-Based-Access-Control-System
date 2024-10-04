import json
from datetime import datetime

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from menu.models import SysRoleMenu
from role.models import SysRole, SysRoleSerializer, SysUserRole



# Create your views here.
class ListAllView(View):

    def get(self, request):
        obj_roleList = SysRole.objects.all().values()  # save as dict
        roleList = list(obj_roleList)                  # save as list
        return JsonResponse({'code': 200, 'roleList': roleList})


# available menu by role
class MenusView(View):

    def get(self, request):
        id = request.GET.get("id")
        menuList = SysRoleMenu.objects.filter(role_id=id).values("menu_id")
        menuIdList = [m['menu_id'] for m in menuList]
        print("menuIdList=", menuIdList)
        return JsonResponse(
            {'code': 200, 'menuIdList': menuIdList})


# grant menu by role
class GrantMenu(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        role_id = data['id']
        menuIdList = data['menuIds']
        print(role_id, menuIdList)
        SysRoleMenu.objects.filter(role_id=role_id).delete()
        for menuId in menuIdList:
            roleMenu = SysRoleMenu(role_id=role_id, menu_id=menuId)
            roleMenu.save()
        return JsonResponse({'code': 200})



class SearchView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        pageNum = data['pageNum']       # current page
        pageSize = data['pageSize'] 
        query = data['query'] 
        print(pageSize, pageNum)
        roleListPage = Paginator(SysRole.objects.filter(name__icontains=query), pageSize).page(pageNum)
        obj_roles = roleListPage.object_list.values()   # save as dict
        roles = list(obj_roles)                         # save as list
        total = SysRole.objects.filter(name__icontains=query).count()
        return JsonResponse(
            {'code': 200, 'roleList': roles, 'total': total})


class SaveView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if data['id'] == -1:   # create
            obj_sysRole = SysRole(name=data['name'], code=data['code'], remark=data['remark'])
            obj_sysRole.create_time = datetime.now().date()
            obj_sysRole.save()
        else:                  # update
            obj_sysRole = SysRole(id=data['id'], name=data['name'], code=data['code'],
                                  remark=data['remark'], create_time=data['create_time'],
                                  update_time=data['update_time'])
            obj_sysRole.update_time = datetime.now().date()
            obj_sysRole.save()
        return JsonResponse({'code': 200})


class ActionView(View):
    # get role by id
    def get(self, request):
        id = request.GET.get("id")
        role_object = SysRole.objects.get(id=id)
        return JsonResponse({'code': 200, 'role': SysRoleSerializer(role_object).data})
    # delete one or many
    def delete(self, request):
        idList = json.loads(request.body.decode("utf-8"))
        SysUserRole.objects.filter(role_id__in=idList).delete()
        SysRoleMenu.objects.filter(role_id__in=idList).delete()
        SysRole.objects.filter(id__in=idList).delete()
        return JsonResponse({'code': 200})