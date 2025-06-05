from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ExamSerializer, Exam


class ExamAPIView(APIView):
    def get(self, request, *args, **kwargs):
        exams = Exam.objects.all()
        serializer_data = ExamSerializer(exams, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)


exam_api_view = ExamAPIView.as_view()
