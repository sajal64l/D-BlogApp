from rest_framework import serializers
from .models import (Blog, BlogComment, BlogTag)
from user.serializer import UserSerializer

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ["title",]

class BlogSerializer(serializers.ModelSerializer):
    tags=BlogTagSerializer(many=True)
    author=UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only =True)
    comment_count = serializers.SerializerMethodField("get_comment_count")

    class Meta:
        model = Blog
        fields = "__all__"

    def get_comment_count(self, obj):
        return obj.blog_comments.count()

class BlogCommentSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)
    blog_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = BlogComment
        fields = "__all__"

