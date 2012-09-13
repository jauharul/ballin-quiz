from django.conf.urls import patterns, include, url
from quiz.models import Quiz, Question, Score

urlpatterns = patterns('quiz.views',
    url(r'^$', 'index'),
    url(r'^(?P<quiz_id>\d+)/$', 'detail'),
    url(r'^(?P<quiz_id>\d+)/results/$', 'results'),
    url(r'^(?P<quiz_id>\d+)/do/$', 'do'),
)
