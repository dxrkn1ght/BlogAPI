from rest_framework import serializers
from author.serializers import AuthorSerializer
from .models import Comment


class RecursiveComment(serializers.Serializer):
    def to_reply_to_parent_comment(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveComment(many=True, read_only=True)
    author_email = serializers.EmailField()
    author = AuthorSerializer



    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'replies']

    def get_replies(self, request, viewer):
        reply = request.data.get("comment")
        if viewer.replies.exists():
            return CommentSerializer(viewer.replies.all(), many=True).data
        return reply

    def validate_parent_comment(self, value):
        max_level = 3
        level = 1
        parent = value

        while parent.parent_comment:
            level += 1
            parent = parent.parent_comment
            if level >= max_level:
                raise serializers.ValidationError(f"Maximum comment nesting level ({max_level}) exceeded.")

        return value

    def validate_author_email(self, value):
        user_domain = value.split('@')[1]
        allowed_domains = ['gmail.com', 'hotmail.com', 'microsoft.com']
        if not value.endswith(allowed_domains):
            raise serializers.ValidationError(f"Sizning {value}@{user_domain} domeni bizning domenlardan : /n{allowed_domains} hech biriga tegishi emas./n Shuning uchun komment yoza olmnaysiz")
        return value.lower()