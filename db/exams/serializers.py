from rest_framework import serializers
from .models import Answer, Exam, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)  # ✅ Nested answers

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answers']

    def create(self, validated_data):
        """Create Question and its related Answers."""
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)

        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)

        return question


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)  # ✅ Nested questions

    class Meta:
        model = Exam
        fields = '__all__'

    def create(self, validated_data):
        """Create Exam along with Questions and Answers."""
        questions_data = validated_data.pop('questions')
        exam = Exam.objects.create(**validated_data)

        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(exam=exam, **question_data)

            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        return exam
