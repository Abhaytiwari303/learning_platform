from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

admin.site.register(Lesson, LessonAdmin)
