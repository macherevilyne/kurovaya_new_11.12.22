
from django.contrib import admin
from django.urls import path, include
from . import views
from users_ import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base),
    path('', include('other.urls')),  # путь на страницу views.homepage
    path('', include('main1.urls')),  # путь на страницу
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', user_views.register, name='register'), # регистрация
]
