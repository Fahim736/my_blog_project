from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # app_name='blog' থাকলে আলাদা করে namespace দিতে হয় না
]