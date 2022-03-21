from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("logout", views.logout, name="logout"),
    path("post/addpost/", views.CreatePost, name="addpost"),
    path("post/update-post/<int:pk>", views.updatePost, name='update_post'),
    path("post/delete-post/<int:pk>", views.deletePost, name='delete_post'),

]
