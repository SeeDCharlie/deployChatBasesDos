from django.urls import path, include
from chat.views import *


urlpatterns = [
    path('', index, name = 'index'),
    path('estados/', api_cStates.as_view(), name = 'getStates'),
    path('logChat/', api_login.as_view(), name = 'api_login'),
    path('logout/', logout_view, name = 'logout'),
    path('', include('rest_framework.urls')),
]   