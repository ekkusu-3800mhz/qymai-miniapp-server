from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200, null=False)
    address = models.TextField(null=False)
    fixedLocation = models.TextField(null=False)
    description = models.TextField(null=True)
    creditPrice = models.CharField(max_length=20, null=True)
    businessTime = models.CharField(max_length=200, null=True)
    remark = models.TextField(null=True)
    createTime = models.DateTimeField(null=False, auto_now_add=True)
    updateTime = models.DateTimeField(null=False, auto_now=True)


class Game(models.Model):
    name = models.CharField(max_length=200, null=False)
    alias = models.CharField(max_length=200, null=False)
    createTime = models.DateTimeField(null=False, auto_now_add=True)
    updateTime = models.DateTimeField(null=False, auto_now=True)


class Cabinet(models.Model):
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    version = models.CharField(max_length=100, null=False)
    credit = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    remark = models.TextField(null=True)
    enablePlayerCount = models.BooleanField(null=False, default=False)
    playerCount = models.IntegerField(null=False, default=0)
    maxCapacity = models.IntegerField(null=False, default=0)
    playerCountUpdateTime = models.DateTimeField(null=True)
    createTime = models.DateTimeField(null=False, auto_now_add=True)
    updateTime = models.DateTimeField(null=False, auto_now=True)
