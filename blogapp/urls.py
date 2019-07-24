from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('newblog/',views.blogpost,name='newblog'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),

]