from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # for HOME
    path('all_employees_', views.all_employees_, name='all_employees_'),
    path('add_employees_', views.add_employees_, name='add_employees_'),
    path('update_employees_', views.update_employees_, name='update_employees_'),
    path('update_employees_/<int:emp_id>', views.update_employees_, name='update_employees_'),
    path('remove_employees_', views.remove_employees_, name='remove_employees_'),
    path('remove_employees_/<int:emp_id>', views.remove_employees_, name='remove_employees_'),
    path('filter_employees_', views.filter_employees_, name='filter_employees_'),
]



