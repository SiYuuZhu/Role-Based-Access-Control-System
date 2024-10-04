from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.settings import api_settings 
from jwt import ExpiredSignatureError, InvalidTokenError, PyJWTError


class JwtAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self,request):
        white_list = ['/user/login','/user/captcha']
        path = request.path
        if path not in white_list and not path.startswith("/media"):
            print('Need Token Authentication')
            token = request.headers.get('AUTHORIZATION')
            print('token:',token)
            try:
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                jwt_decode_handler(token)
            except ExpiredSignatureError:
                return HttpResponse('Token is expired, please login again!')
            except InvalidTokenError:
                return HttpResponse('Token invalid')
            except PyJWTError:
                return HttpResponse('Token error')
        else:
            print("No need to token authentication")
            return None
