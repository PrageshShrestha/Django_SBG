from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello,name = 'SBGS'),
    path('1/' , views.hello2 , name = 'Login')
]
urlpatterns += staticfiles_urlpatterns()