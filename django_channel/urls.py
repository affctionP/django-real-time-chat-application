from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts.views import get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat_app.urls')),
    path('',get_data),
    
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]
