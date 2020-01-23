from django.contrib import admin
from django.urls import path

from questionPlatform import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_questions, name="add_question"),
    path('question/answers/<id>/', views.answers, name="questions_answers"),
    path('question/post_ans/<id>/', views.post_answer, name="post_answers"),
<<<<<<< HEAD
    path('quesion/delete/<id>', views.delete_question, name="delete_question"),

=======
>>>>>>> 3a97565c7bbbb4da3f63408236d0ce6125cffe70
]