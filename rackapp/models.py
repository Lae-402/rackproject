from django.db import models
from accounts.models import CustomUser

class Media(models.Model):
    title = models.CharField(
        verbose_name="媒体",
        max_length=20)
    def __str__(self):
        return self.title

class Artist(models.Model):
    title = models.CharField(
        verbose_name="アーティスト",
        max_length=40)
    def __str__(self):
        return self.title


class Rack(models.Model):

    user = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザー",
        on_delete=models.CASCADE
    )

    title = models.CharField(
        verbose_name="タイトル",
        max_length=100)
    
    ruby = models.CharField(
        verbose_name="ふりがな",
        max_length=200
    )

    media = models.ForeignKey(
        Media,
        verbose_name="媒体",
        on_delete=models.PROTECT)

    artist = models.ForeignKey(
        Artist,
        verbose_name="アーティスト",
        on_delete=models.PROTECT)
    
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )