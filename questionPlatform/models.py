from django.db import models
from django.conf import settings


# creating question class to post the question and store the posted questions in the database
class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    ans_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    commented_date = models.DateTimeField(auto_now_add=True)
    # is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

