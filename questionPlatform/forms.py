from django import forms
from questionPlatform.models import Question
# from .models import Answer


class questionForm(forms.ModelForm):
    # form betra meta data
    class Meta:
        model = Question
        fields = ('question_text', 'post_date')
