from django.db import models
#from django.contrib.auth.models import User
from random import shuffle

class Quiz(models.Model):
    """ Quiz model. Every quiz has 10 questions. """
    title       = models.CharField(max_length=100)
    category    = models.CharField(max_length=100)
    description = models.TextField()
    slug        = models.SlugField(unique=True)
#	author      = models.ForeignKey(User, related_name='author')
    author      = models.CharField(max_length=50)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'quizzes'
        ordering            = ('-modified', 'created')
        
    def __unicode__(self):
        return u"%s" % self.title
        
    def options(self):
        return list('abcde')
        
class Question(models.Model):
    """ Question model. Each question attached to exact one quiz. """
    quiz     = models.ForeignKey(Quiz)
    question = models.TextField()
    answer   = models.TextField()
    choice1  = models.TextField()
    choice2  = models.TextField()
    choice3  = models.TextField()
    choice4  = models.TextField()
    
    class Meta:
        ordering = ('id', 'question',)
        
    def __unicode__(self):
        return u"%s" % self.question
    
    def get_options(self):
        return {'answer': self.answer, 'choice1': self.choice1, 'choice2': self.choice2, 'choice3':self.choice3, 'choice4': self.choice4, }
        
    def randomize_options(self):
        options = ['answer', 'choice1', 'choice2', 'choice3', 'choice4', ]
        shuffle(options)
        return options
        
class Score(models.Model):
    """ Score model. Every quiz taken by students are recorded here. """
    quiz          = models.ForeignKey(Quiz)
    student       = models.CharField(max_length=50)
    submit_answer = models.CharField(max_length=50)
    score         = models.IntegerField(default=0)
    quiz_taken    = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering  = ('quiz_taken', 'student', 'score',)
        
    def __unicode__(self):
        return u"%s %d" % (student, score)