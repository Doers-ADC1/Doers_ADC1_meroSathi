from django.contrib import admin
from django.urls import path

from questionPlatform import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('add/', views.add_questions, name="add_question"),
    path('question/answers/<id>/', views.answers, name="questions_answers"),
    path('question/post_ans/<id>/', views.post_answer, name="post_answers"),
    path('question/edit_ques/<id>', views.edit_question, name = "edit_question"),
    path('quesion/delete/<id>', views.delete_question, name="delete_question"),
]