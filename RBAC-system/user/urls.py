from django.urls import path

from user.views import ActionView, AvatarView, CaptchaView, CheckView, GrantRole, ImageView, LoginView, JwtTestView, PwdView, ResetPasswordView, SaveView, SearchView, StatusView, TestView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('save', SaveView.as_view(), name='save'),
    path('updateUserPwd', PwdView.as_view(), name='updateUserPwd'),
    path('uploadImage', ImageView.as_view(), name='uploadImage'),
    path('updateAvatar', AvatarView.as_view(), name='updateAvatar'), 
    path('search', SearchView.as_view(), name='search'), 
    path('action', ActionView.as_view(), name='action'), 
    path('check', CheckView.as_view(), name='check'),
    path('status', StatusView.as_view(), name='status'),
    path('resetPassword', ResetPasswordView.as_view(), name='resetPassword'),
    path('grantRole',GrantRole.as_view(),name='grant'),
    path('captcha', CaptchaView.as_view(), name='captcha'),
    
    path('test', TestView.as_view(), name='test'), 
    path('jwt_test', JwtTestView.as_view(), name='jwt_test'), 
]
