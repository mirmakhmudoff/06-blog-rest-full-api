from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


class MyBlogsView(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)


class AddCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_id']
        blog = Blog.objects.get(id=blog_id)
        serializer.save(user=self.request.user, blog=blog)


@api_view(['POST'])
def like_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
    else:
        blog.likes.add(request.user)
        return Response({'message': 'Liked'}, status=status.HTTP_200_OK)