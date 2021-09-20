from django.urls import path
from . import views

urlpatterns=[
    path('todos/',views.TodosView.as_view(),name='todos'),
    path('todo/<int:id>/',views.TodoView.as_view(),name='todo')
]