from django.db import models
from django.contrib.auth.models import User

  
class QuestionManager(models.Manager):
  def new(self):
    return self.orderby('-added_at').all()
  
  def popolar(self):
    return self.orderby('-rating').all()
  
class Likes(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="like_question"
    )
    user = models.ForeignKey(
        User,
        related_name="like_user"
    )  

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank = True, auto_now_add=True)
  rating = models.IntegerField(default = 0)
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(User, through="Likes")
  objects = QuestionManager()


  
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(blank = True, auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)
