from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('', views.home, name="home"),
    #path('about/', views.about, name="about"),
    #path('book', views.book, name="book"),
    #path('menu/', views.menu, name="menu"),
    #path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]