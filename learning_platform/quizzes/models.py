from django.db import models
from lessons.models import Lesson
from accounts.models import User

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    submitted_answer = models.TextField()
    correct = models.BooleanField(default=False)