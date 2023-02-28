from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from BlogApplication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('add/',addBlog,name='addblog'),
    path('like/<str:pk>',likeBlog,name='like'),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)