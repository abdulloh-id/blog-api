from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post.show'),
    path('', PostList.as_view(), name='post.index'),
]
