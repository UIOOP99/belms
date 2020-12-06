from lms.handlers import grpc_handlers as lms_grpc_handlers
from django.contrib import admin
from django.urls import path, include    
from rest_framework import routers
from lms import views

router = routers.DefaultRouter()                      
router.register(r'lms', views.MessageView, 'lms')     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]


def grpc_handlers(server):
    lms_grpc_handlers(server)
