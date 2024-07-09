from django.urls import path
from .views import MenuItemView, SingleMenuItemView, index


urlpatterns = [
    path('', index, name='index'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
    path('menu/', MenuItemView.as_view(), name='menu_item')
]





