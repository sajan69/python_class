from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post-details/<int:id>', views.post_details, name="post-details"),
    path('create-post', views.create_post, name="create-post"),
    path('register', views.registerUser, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('login', views.login_user, name="login"),

]
