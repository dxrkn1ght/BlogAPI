from rest_framework import serializers
from .models import Post
from category.serializers import CategorySerializer
from author.serializers import AuthorSerializer
from tag.serializers import TagSerializer
from comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'slug', 'created_at', 'updated_at', 'status', 'comment_count', 'comments']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value

    def validate_status(self, value):
        if value not in ['active', 'pending', 'inactive']:
            raise serializers.ValidationError("Invalid status value.")
        return value

    def get_comment_count(self, obj):
        return obj.comments.count() if hasattr(obj, 'comments') else 0

    def create(self, validated_data):
        validated_data['slug'] = validated_data.get('slug') or slugify(validated_data['title'])
        return super().create(validated_data)