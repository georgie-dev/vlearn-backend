from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Quiz, QuesModel
from rest_framework.decorators import action
from .serializer import QuizSerializer, QuestionSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

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
    @action(detail=False, methods=['GET'])
    def filter_by_course(self, request):
        course_codes = self.request.query_params.get('course', '')
        
        if course_codes:
            course_code_list = course_codes.split(',')
            tests = self.queryset.filter(course__in=course_code_list)
            serialized_classes = self.serializer_class(tests, many=True)
            return Response(serialized_classes.data)
        else:
            return Response("No course codes provided", status=status.HTTP_400_BAD_REQUEST)
    
class QuestionViewSet(APIView):
    def get(self, request, *args, **kwargs):
        questions = QuesModel.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        questions_data = request.data  # Array of question objects

        serializer = QuestionSerializer(data=questions_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizSubmissionViewSet(viewsets.ViewSet):
    def create(self, request):
        quiz_id = request.data.get('quiz_id')
        original_order = request.data.get('original_order')
        answers = request.data.get('answers')

        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

        questions = QuesModel.objects.filter(quiz=quiz)

        score = 0
        wrong = 0
        correct = 0
        total_marks = 0

        for answer in answers:
            total_marks += 1
            question_id = answer.get('question_id')
            
            if question_id is None or question_id >= len(original_order):
                return Response({'error': f'Invalid question_id: {question_id}'}, status=status.HTTP_400_BAD_REQUEST)

            original_question_id = original_order[question_id]

            try:
                question = next(q for q in questions if q.id == original_question_id)
            except StopIteration:
                return Response({'error': f'Question with ID {original_question_id} not found'}, status=status.HTTP_400_BAD_REQUEST)

            selected_option = answer.get('selected_option')

            if selected_option == question.correct_option:
                score += 10
                correct += 1
            else:
                wrong += 1

        percent = score / (total_marks * 10) * 100

        return Response({
            'score': score,
            'time': request.data.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total_marks
         }, status=status.HTTP_200_OK)

