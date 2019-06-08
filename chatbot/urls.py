from django.contrib import admin
from django.urls import path, include

from .views import 챗뷰, chatAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', 챗뷰.as_view(), name='챗뷰'),
    path('api/', chatAPI, name='chatAPI'),
]