from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250)
    date_joined = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='following')

    def __str__(self):
        return self.username

class Friend(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='friend_creator_set')
    friend = models.ForeignKey(User,related_name='Friend')

    def __str__(self):
        return self.friend

class Posts(models.Model):
    user = models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    post = models.CharField(max_length=250)
    published_on = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField()

    class Meta:
        ordering = ['published_on']
        

    def __str__(self):
        return self.post

class Comment(models.Model):
    post = models.ForeignKey(Posts,related_name='comment', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.comment