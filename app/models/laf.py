from django.db import models


class LAF(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    type = models.IntegerField(default=1, null=False)
    status = models.IntegerField(default=0, null=False)
    time = models.CharField(max_length=100, null=False)
    location = models.TextField(null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    photo = models.TextField(null=True)
    contact = models.TextField(null=False)
    createTime = models.DateTimeField(null=False, auto_now_add=True)
    updateTime = models.DateTimeField(null=False, auto_now=True)
