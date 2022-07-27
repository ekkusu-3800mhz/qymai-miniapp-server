from django.db import models


class User(models.Model):
    openId = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    avatar = models.TextField(null=True)
    qqUim = models.CharField(max_length=50, null=True)
    emailHash = models.CharField(max_length=6, null=True)
    createTime = models.DateTimeField(null=False, auto_now_add=True)
    updateTime = models.DateTimeField(null=False, auto_now=True)
