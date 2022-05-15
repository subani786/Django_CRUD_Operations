from django.urls import path
from . import views

urlpatterns = [
    path('',views.addandshow,name='addandshow'),
    path('delete/<int:id>',views.studdelete,name="delete"),
    path('edit/<int:id>',views.editstu,name="edit"),
]
