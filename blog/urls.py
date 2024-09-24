from django.urls import path
from .views import BlogListView, BlogDetailView, MyBlogsView, AddCommentView, like_blog

urlpatterns = [
    path('blogs/', BlogListView.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view()),
    path('my-blogs/', MyBlogsView.as_view()),
    path('blogs/<int:blog_id>/comment/', AddCommentView.as_view()),
    path('blogs/<int:blog_id>/like/', like_blog),
]