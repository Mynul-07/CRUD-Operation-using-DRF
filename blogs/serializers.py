from rest_framework import serializers  # Import DRF’s serializers module for building APIs.
from blogs.models import Blog, Comment  # Import Blog and Comment models from your ‘blogs’ app.

# Comment serializer
class CommentSerializer(serializers.ModelSerializer):  # Inherit from ModelSerializer (auto-handles model fields).
    class Meta:
        model = Comment  # Tells DRF this serializer is for the Comment model.
        fields = '__all__'  # Include all fields in the Comment model.

# Blog serializer
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Nested serializer: Blog has many comments.

    class Meta:
        model = Blog  # Tells DRF this serializer is for the Blog model.
        fields = ['id', 'blog_title', 'blog_body', 'comments']  # Include all fields in the Blog model.
