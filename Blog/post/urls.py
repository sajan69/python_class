from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post-detail/<int:id>/', views.post_details, name="post-details"),
    path('create-post', views.create_post, name="create-post")
]
