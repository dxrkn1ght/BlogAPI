from django.db import models
from post.models import Post
from author.models import Author


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    def save(self, *args, **kwargs):
        author, created = Author.objects.get_or_create(email=self.author_email, defaults={"name": self.author_name})
        self.author = author
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.author.name} on {self.post.title}"