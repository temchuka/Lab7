from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    path('lease/new/', views.create_lease, name='create_lease'),
    re_path(r'^lease/(?P<lease_id>\d+)$', views.get_lease, name='get_lease'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
