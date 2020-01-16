from django.db import models

#creating question class to post the question and store the posted questions in the database
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    post_date = models.DateTimeField('Post Date')

    def __str__(self):
        return self.question_text

class Answer(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        answer_text = models.CharField(max_length=1000)
        is_favorite = models.BooleanField(default=False)

        def __str__(self):
            return self.question


