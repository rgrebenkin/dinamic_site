from django.db import models
from django.contrib.auth.models import User

  
class QuestionManager(models.Manager):
  def new(self):
    return self.orderby('-added_at').all()
  
  def popolar(self):
    return self.orderby('-rating').all()
  

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(User)
  objects = QuestionManager()


  
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)
