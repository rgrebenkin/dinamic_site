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
  added_at = models.DateField()
  rating = models.FloatField()
  author = models.ForeignKey(User, default='x')
  likes = models.ForeignKey(User, default='x')
  objects = QuestionManager()


  
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField()
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User, default='x')
