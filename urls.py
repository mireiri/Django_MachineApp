from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('predict/', views.predict, name='predict'),
    path('predict_exe/', views.predict_exe, name='predict_exe'),
    path('graph/', views.graph, name='graph'),
    path('graph_exe/<int:id>/', views.graph_exe, name='graph_exe'),
    path('dd/', views.dd, name='dd'),
    path('download/<str:path>/', views.download, name='download'), 
    path('output_delete/<str:path>/', views.output_delete, name='output_delete'),
    path('lecture/', views.lecture, name='lecture'),      
]     

