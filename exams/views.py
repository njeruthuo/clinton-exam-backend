from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ExamSerializer, Exam


class ExamAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Exam.objects.prefetch_related('questions__answers')
        serializer_data = ExamSerializer(queryset, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)


exam_api_view = ExamAPIView.as_view()
