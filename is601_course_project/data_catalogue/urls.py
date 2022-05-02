from django.urls import include, path


from . import views
from .views import Home

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'data_catalogue_desc', views.DataSetDescViewSet)


urlpatterns = [
    #path('',views.index,name='index'),
    #path('home', Home.as_view(), name='home'),
    path('',Home.as_view(), name='home'),

    path('dataview', views.dataview, name='dataview'),
    path('datasets', views.datasets, name='datasets'),
    path('tabview/<name>/<env>/', views.tabview, name='tabview'),
    path('ajax', views.ajax, name='ajax'),
    path('ajax-demo', views.ajax_demo, name='ajax-demo'),
    path('api/', include(router.urls) ),
]