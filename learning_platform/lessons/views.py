from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Lesson
from .serializers import LessonSerializer
from courses.models import Course

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow all authenticated users to view lessons
        return Lesson.objects.all()

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise PermissionDenied("Course does not exist.")

        # DEBUG log to confirm
        print("📢 request.user.id:", self.request.user.id)
        print("📢 course.instructor.id:", course.instructor.id)

        if not self.request.user.is_instructor:
            raise PermissionDenied("Only instructors can add lessons.")

        if course.instructor.id != self.request.user.id:
            raise PermissionDenied("You are not the instructor of this course.")

        serializer.save(course=course)
