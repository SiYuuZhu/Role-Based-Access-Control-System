from django.urls import path

from role.views import ListAllView, SearchView, SaveView, ActionView, MenusView, GrantMenu

urlpatterns = [
    path('listAll', ListAllView.as_view(), name='listAll'),
    path('search', SearchView.as_view(), name='search'),
    path('save', SaveView.as_view(), name='save'), 
    path('action', ActionView.as_view(), name='action'),
    path('grant', GrantMenu.as_view(), name='grant'),
    path('menus', MenusView.as_view(), name='menus'),
]
