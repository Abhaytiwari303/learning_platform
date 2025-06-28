from rest_framework import serializers
from .models import Quiz, Submission

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

    def create(self, validated_data):
        quiz = validated_data['quiz']
        submitted_answer = validated_data['submitted_answer']
        correct = (submitted_answer.strip().lower() == quiz.answer.strip().lower())
        validated_data['correct'] = correct
        return super().create(validated_data)
