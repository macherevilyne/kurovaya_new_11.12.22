
from django.urls import path
from .import views


#     path('delete-item/<int:id>/',views.deletecarrier, name='delete-сarrier', ), # Удаление созданных обьектов
#  path('delete-item/<int:pk>/)/$',views.deletecarrier, name='delete-сarrier', ), # Удаление созданных обьектов
urlpatterns = [
    path('actual/', views.actual, name='actual'),  # путь на страницу views.homepage
    path('carrier/', views.carrier, name='carrier'),  # путь на страницу, где name для указанием URLS в маршрутах
    path('delete-item/<int:carrier_id>/',views.deletecarrier, name='delete-сarrier', ), # Удаление созданных обьектов
]

