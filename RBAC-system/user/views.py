import base64
from datetime import datetime
import hashlib
from io import BytesIO
import json
import random
import uuid
from RBAC_admin import settings
from captcha.image import ImageCaptcha


from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.core.cache import cache

from menu.models import SysMenu, SysMenuSerializer
from role.models import SysRole, SysUserRole
from user.models import SysUser, SysUserSerializer
from rest_framework_jwt.settings import api_settings



class LoginView(View):

    def buildMenuTree(self,sysMenuList):
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

    def post(self,request):
        username = request.GET.get("username")
        password = request.GET.get("password")
        pwd_md5 = hashlib.md5(password.encode()).hexdigest()
        code = request.GET.get("code")
        uuid = request.GET.get("uuid")
        captcha = cache.get(uuid)
        print(captcha)
        if captcha == '' or captcha.lower() != code.lower():
            return JsonResponse({'code':500, 'info':'驗證碼錯誤'})
        try:
            user = SysUser.objects.get(username=username, password=pwd_md5)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            # Get Menu set from user role
            roleList = SysRole.objects.raw("SELECT id,NAME FROM sys_role WHERE id IN ( SELECT role_id FROM sys_user_role WHERE user_id="+str(user.id)+")")
            print(roleList)
            menuSet: set[SysMenu] = set()
            for r in roleList:
                print(r.id, r.name)
                menuList = SysMenu.objects.raw("SELECT * FROM sys_menu WHERE id IN (SELECT menu_id FROM sys_role_menu WHERE role_id=" + str(r.id) + ")")
                for m in menuList:
                    print(m.id, m.name, m.menu_type)
                    menuSet.add(m)
            print(menuSet)
            # convert to list & sort by order_num
            menuList: list[SysMenu] = list(menuSet)
            sorted_menuList = sorted(menuList)
            print(sorted_menuList)
            # construct the menu tree
            SysMenuList: list[SysMenu] = self.buildMenuTree(sorted_menuList)
            print(SysMenuList)
            serializerMenuList = list()
            for sysMenu in SysMenuList:
                serializerMenuList.append(SysMenuSerializer(sysMenu).data)

            # get current user roles
            roles = ",".join([r.name for r in roleList])

        except Exception as e:
            print(e)
            return JsonResponse({'code':500, 'info':'帳號或密碼錯誤'})
        return JsonResponse({'code':200, 
                             'token':token,
                             'user':SysUserSerializer(user).data,
                             'menuList': serializerMenuList,
                             'roles': roles,
                             'info':'登入成功'})


class SaveView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        if data['id'] == -1:  #new
            obj_sysUser = SysUser(username=data['username'], password=data['password'],
                                  email=data['email'], phonenumber=data['phonenumber'],
                                  status=data['status'], remark=data['remark'])
            obj_sysUser.create_time = datetime.now().date()
            obj_sysUser.avatar = 'default.jpg'
            obj_sysUser.password = hashlib.md5("123456".encode()).hexdigest()
            obj_sysUser.save()
        else:                 #save for change
            obj_sysUser = SysUser(id=data['id'], username=data['username'], password=data['password'],
                                  avatar=data['avatar'], email=data['email'], phonenumber=data['phonenumber'],
                                  login_date=data['login_date'], status=data['status'], create_time=data['create_time'],
                                  update_time=data['update_time'], remark=data['remark'])
            obj_sysUser.update_time = datetime.now().date()
            obj_sysUser.save()

        return JsonResponse({'code': 200, 'info':'儲存使用者成功'})


class StatusView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        status = data['status']
        user_object = SysUser.objects.get(id=id)
        user_object.status = status
        user_object.save()
        return JsonResponse({'code': 200})


class ResetPasswordView(View):

    def get(self, request):
        id = request.GET.get("id")
        user_object = SysUser.objects.get(id=id)
        user_object.password = hashlib.md5("123456".encode()).hexdigest()
        user_object.update_time = datetime.now().date()
        user_object.save()
        return JsonResponse({'code': 200})


# Check for repeat username
class CheckView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        username = data['username']
        print("username=", username)
        if SysUser.objects.filter(username=username).exists():
            return JsonResponse({'code': 500, 'info':'新使用者名稱已存在'})
        else:
            return JsonResponse({'code': 200, 'info':'新使用者名稱OK'})


class ActionView(View):
    # get user info by id
    def get(self, request):
        id = request.GET.get("id")
        user_object = SysUser.objects.get(id=id)
        return JsonResponse({'code': 200, 'user': SysUserSerializer(user_object).data})
    # Delete user & its role
    def delete(self, request):
        idList = json.loads(request.body.decode("utf-8"))
        SysUserRole.objects.filter(user_id__in=idList).delete()
        SysUser.objects.filter(id__in=idList).delete()
        return JsonResponse({'code': 200})


class GrantRole(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        user_id = data['id']
        roleIdList = data['roleIds']
        print(user_id, roleIdList)
        SysUserRole.objects.filter(user_id=user_id).delete()
        for roleId in roleIdList:
            userRole = SysUserRole(user_id=user_id, role_id=roleId)
            userRole.save()
        return JsonResponse({'code': 200})


class PwdView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        oldPassword = data['oldPassword']
        newPassword = data['newPassword']
        obj_user = SysUser.objects.get(id=id)
        if hashlib.md5(oldPassword.encode()).hexdigest() == obj_user.password:
            obj_user.password = hashlib.md5(newPassword.encode()).hexdigest()
            obj_user.update_time = datetime.now().date()
            obj_user.save()
            return JsonResponse({'code': 200, 'info':'成功修改密碼'})
        else:
            return JsonResponse({'code': 500, 'info':'原密碼輸入錯誤'})


class ImageView(View):

    def post(self, request):
        file = request.FILES.get('avatar')
        print("file:", file)
        if file:
            file_name = file.name
            suffix_fileFormat = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffix_fileFormat
            file_path = str(settings.MEDIA_ROOT) + "\\userAvatar\\" + new_file_name
            print("file_path:", file_path)
            try:
                with open(file_path, 'wb') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                return JsonResponse({'code': 200, 'title': new_file_name, 'info':'頭像檔案已保存於server'})
            except:
                return JsonResponse({'code': 500, 'info': '上傳頭像失敗，請檢查網路'})
            

class AvatarView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        avatar = data['avatar']
        obj_user = SysUser.objects.get(id=id)
        obj_user.avatar = avatar
        obj_user.save()
        return JsonResponse({'code': 200, 'info':'頭像更新成功'})
    

# search for all/query & Pagination
class SearchView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        pageNum = data['pageNum']       # current page
        pageSize = data['pageSize']
        query = data['query']
        print(pageSize, pageNum)
        userListPage = Paginator(SysUser.objects.filter(username__icontains=query), pageSize).page(pageNum)
        print(userListPage)
        obj_users = userListPage.object_list.values()   # save as dict
        users = list(obj_users)                         # sava as list 
        total = SysUser.objects.filter(username__icontains=query).count()
        # get roles of user
        for user in users:
            userId = user['id']
            roleList = SysRole.objects.raw("SELECT id,name FROM sys_role WHERE id IN (SELECT role_id FROM sys_user_role WHERE user_id =" + str(userId) + ")")
            roleListDict = []
            for role in roleList:
                roleDict = {}
                roleDict['id'] = role.id
                roleDict['name'] = role.name
                roleListDict.append(roleDict)
            user['roleList'] = roleListDict
        return JsonResponse({'code': 200,
                             'userList': users,
                             'total':total,
                             'info':'search user and paged'})


class CaptchaView(View):

    def get(self,request):
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        data = ''.join(random.sample(characters, 4))
        print("captcha", data)
        captcha = ImageCaptcha()
        imageData: BytesIO = captcha.generate(data)
        base64_str = base64.b64encode(imageData.getvalue()).decode()
        random_uuid = uuid.uuid4() 
        print(random_uuid)
        cache.set(random_uuid, data, timeout=300)   # redis for 300s
        print("redis check",cache.has_key(random_uuid))
        return JsonResponse({'code': 200, 'base64str': 'data:image/png;base64,' + base64_str, 'uuid': random_uuid})




class TestView(View):

    def get(self,request):
        token = request.headers.get('AUTHORIZATION')
        if token != None and token !='':
            userList_obj = SysUser.objects.all()
            print(userList_obj,type(userList_obj))
            userList_dict = userList_obj.values()
            print(userList_dict,type(userList_dict))
            userList = list(userList_dict)
            print(userList,type(userList))
            return JsonResponse({'code': 200, 'info':'TEST','data':userList})
        else:
            return JsonResponse({'code': 401, 'info':'no authorization to visit!'})


class JwtTestView(View):

    def get(self, request):
        user = SysUser.objects.get(username='yuuu',password='123456')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # get payload of this user
        payload = jwt_payload_handler(user)
        # encode as JWT format
        token = jwt_encode_handler(payload)
        return JsonResponse({'code':200,'token':token})