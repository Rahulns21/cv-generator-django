from django.urls import path
from . import views

app_name = 'cv'
urlpatterns = [
    path('', views.accept, name='accept'),
    path('list/', views.list, name='list'),
    path('list/cv/<int:id>', views.resume, name='resume'),
]