from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import QuizViewSet, SubmissionViewSet, SubmitQuizView

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('submit/<int:quiz_id>/', SubmitQuizView.as_view(), name='submit-quiz'),
]
