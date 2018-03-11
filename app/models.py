from django.db import models


# Create your models here.
# 用户
class User(models.Model):
    # 密码
    u_password = models.CharField(max_length=32)
    # 昵称
    u_name = models.CharField(max_length=20, primary_key=True)
    # 头像路径
    u_icon = models.ImageField(upload_to='icons')
    isDelete = models.BooleanField(default=False)
    email = models.CharField(null=True, max_length=16, unique=True)


class Banner(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image')
    desc = models.CharField(max_length=200)


class Movies(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    postid = models.IntegerField()
    image = models.ImageField(upload_to='image')
    like_num = models.IntegerField(default=0)
    request_url = models.CharField(max_length=200, null=True)


class Like(models.Model):
    like_user = models.ForeignKey(User)
    like_movies = models.ForeignKey(Movies)
