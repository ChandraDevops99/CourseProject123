from django.contrib import admin
from django.urls import path
from courseApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.course_list, name='course_list'),
    path('course/new/', views.course_create, name='course_create'),
    path('course/<int:pk>/edit/', views.course_update, name='course_update'),
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),
]

