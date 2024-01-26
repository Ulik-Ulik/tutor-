
from django.contrib import admin
from django.urls import path
from blog.views import index, john

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('john-name-info/', john, name='john'),
]
