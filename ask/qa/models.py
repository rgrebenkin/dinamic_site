from django.db import models
from django.contrib.auth.models import User

  
class QuestionManager(models.Manager):
  def new(self):
    return self.orderby('-added_at').all()
  
  def popular(self):
    return self.orderby('-rating').all()

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank = True, auto_now_add=True)
  rating = models.IntegerField(default = 0)
  author = models.ForeignKey(User, related_name='question_author')
  #author = models.CharField(max_length=255)
  #likes = models.ManyToManyField(User, through="Likes")
  likes = models.ManyToManyField(User)
  objects = QuestionManager()
  
  def __unicode__(self) :
    return self.title
  
  def get_url(self):
    return reverse('question', kwargs = { 'id': self.id })  

  
#class Likes(models.Model):
#    question = models.ForeignKey(
#        Question,
#        related_name="like_question"
#    )
#    user = models.ForeignKey(
#        User,
#        related_name="like_user"
#    )  

  
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(blank = True, auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)
  #author = models.CharField(max_length=255)
  
  def __unicode__(self):
    return self.text
