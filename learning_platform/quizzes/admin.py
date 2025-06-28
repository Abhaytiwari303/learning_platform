from django.contrib import admin
from .models import Quiz, Submission

class QuizAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'question')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'submitted_answer', 'correct')

admin.site.register(Quiz)
admin.site.register(Submission)
