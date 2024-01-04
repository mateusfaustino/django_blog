from django.urls import path
from posts.views import posts, post

urlpatterns = [
    path('', post),
    path('todos', posts),
]