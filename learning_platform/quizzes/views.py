from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, Submission
from accounts.models import User
from rest_framework import viewsets
from .models import Quiz, Submission
from .serializers import QuizSerializer, SubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsInstructor
from rest_framework import viewsets, permissions


class SubmitQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id):
        answer = request.data.get('answer')
        quiz = Quiz.objects.get(id=quiz_id)
        correct = quiz.answer.strip().lower() == answer.strip().lower()

        submission = Submission.objects.create(
            user=request.user,
            quiz=quiz,
            submitted_answer=answer,
            correct=correct
        )
        from rest_framework import status

        return Response({'result': 'correct' if correct else 'wrong'}, status=status.HTTP_201_CREATED)

    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)