from django.contrib import admin
import nested_admin
from .models import Exam, Question, Answer


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 2  # Number of empty forms displayed


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1  # Number of empty forms displayed
    inlines = [AnswerInline]  # Nest Answers inside Questions


class ExamAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]  # Nest Questions inside Exams


admin.site.register(Exam, ExamAdmin)
