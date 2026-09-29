from django.urls import path
from . import views

app_name = 'blog'  # <-- এই লাইনটি অবশ্যই থাকতে হবে

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/new/', views.create_post_view, name='create_post'),
    path('post/<int:pk>/edit/', views.edit_post_view, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),
    path('my-posts/', views.my_posts_view, name='my_posts'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/<int:pk>/comment/', views.add_comment_view, name='add_comment'),
    path('post/<int:pk>/rate/', views.rate_post, name='rate_post'),
]