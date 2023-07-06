from letslearn import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.index, name = 'index'),
    path('sky',views.say, name = 'say'),
    path("add/",views.add, name = "add"),
    path("add/addrecord/", views.addrecord, name = "addrecord"),
    path("delete/<int:id>", views.delete, name = "delete"),
    path("update/<int:id>", views.update, name = "update"),
    path("update/updaterecord/<int:id>", views.updaterecord, name = "updaterecord")
]
