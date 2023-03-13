from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workers', views.workers_list_view, name='workers'),
    path('worker/update/<int:pk>/', views.WorkerUpdate.as_view(), name='worker_update'),
]
