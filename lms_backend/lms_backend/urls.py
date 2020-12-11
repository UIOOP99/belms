
from django.contrib import admin
from django.urls import path ,include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token', obtain_jwt_token),
    path('lms/', include('lms.urls')),

]

"""
curl -X POST -d "username=admin&password=password123" http://127.0.0.1:8000/api/auth/token
"""
