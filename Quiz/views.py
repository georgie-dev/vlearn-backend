from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Quiz, QuesModel
from .filters import QuizFilterSet
from .serializer import QuizSerializer, QuestionSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class= QuizFilterSet

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"id": serializer.data["id"]},  # Return the created quiz's ID
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuesModel.objects.all()
    serializer_class = QuestionSerializer

class QuizSubmissionViewSet(viewsets.ViewSet):
    def create(self, request):
        quiz_id = request.data.get('quiz_id')
        answers = request.data.get('answers')  # List of user's answer choices

        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)
        score=0
        wrong=0
        correct=0
        total_marks = 0
        for answer in answers:
            total_marks +=1
            question_id = answer.get('question_id')
            selected_option = answer.get('selected_option')

            try:
                question = QuesModel.objects.get(pk=question_id)
            except QuesModel.DoesNotExist:
                return Response({'error': f'Question with ID {question_id} not found'}, status=status.HTTP_400_BAD_REQUEST)

            if selected_option == question.correct_option:
                score+=10
                correct+=1
            else:
                wrong += 1
            percent = score/(total_marks*10) *100

        return Response({
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total_marks
        }, status=status.HTTP_200_OK)
