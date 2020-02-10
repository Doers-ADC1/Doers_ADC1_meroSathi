from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from questionPlatform import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('add/', views.add_questions, name="add_question"),
    path('question/answers/<id>/', views.answers, name="questions_answers"),
    path('question/post_ans/<id>/', views.post_answer, name="post_answers"),
    path('question/edit_ques/<id>', views.edit_question, name = "edit_question"),
    path('quesion/delete/<id>', views.delete_question, name="delete_question"),
    path('search/', views.search, name='search'),
    path('myposts/', views.own_posts,name='myposts'),
    path('latestposts/', views.latest_posts, name='latestposts'),
    url(r'^squestions/', views.QuestionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

