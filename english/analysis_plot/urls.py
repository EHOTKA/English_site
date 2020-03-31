from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('analys', views.analys, name='analys')
]