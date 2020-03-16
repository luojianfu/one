from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('node_stats/',views.node_stats,name='node_stat'),
    path('node_start/<str:domain_name>',views.node_start,name='node_start'),
    path('node_action/<str:action>/<str:domain_name>',views.node_action,name='node_action'),
    path('node_shutdown/<str:domain_name>', views.node_shutdown, name='node_shutdown'),
]