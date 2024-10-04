from django.urls import path

from menu.views import TreeListView, ActionView, SaveView

urlpatterns = [
    path('treeList', TreeListView.as_view(), name='treeList'),
    path('action', ActionView.as_view(), name='action'),
    path('save', SaveView.as_view(), name='save'), 
]
