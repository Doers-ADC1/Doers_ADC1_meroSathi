from django import forms

from .models import Question
from .models import Answer

class OurForm(forms.ModelForm):
    #form betra meta data
    class Meta:
        model = Question
        fields = ('Question_text', 'post_date')

    class Meta:
        model = Answer
        fields = ('question', 'answer_text', 'is_favorite')
