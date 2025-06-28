from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from accounts.permissions import IsInstructor
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Only instructors can create
        if not self.request.user.is_instructor:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only instructors can create courses.")
        serializer.save(instructor=self.request.user)

