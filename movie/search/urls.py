from django.conf.urls import url
from django.urls import path, include
from .import views



# SET THE NAMESPACE!
# app_name = 'profile'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns=[

    path('', views.index, name='index'),
    path('movie/<id>/', views.single_movie, name='single_movie'),
    path('favorite/<id>/', views.make_favorite, name='make_favorite'),
    path('favorite/<id>/remove/', views.remove_favorite, name='remove_favorite'),
    path('favorite/', views.favorite, name='favorite'),

]