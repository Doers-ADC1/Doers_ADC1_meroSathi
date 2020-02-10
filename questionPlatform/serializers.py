from rest_framework import serializers
from questionPlatform.models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'post_date')