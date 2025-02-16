from django.contrib import admin
from .models import Exam, Question, Answer


class AnswerInline(admin.TabularInline):  # Inline for Answers
    model = Answer
    extra = 2  # Allows adding extra answers per question


class QuestionInline(admin.TabularInline):  # Inline for Questions
    model = Question
    extra = 1  # Allows adding extra questions


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show Exam details in the list view
    search_fields = ('name',)  # Allow searching by name
    inlines = [QuestionInline]  # Allows adding Questions from Exam page


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'get_first_answer')
    search_fields = ('exam__name',)
    inlines = [AnswerInline]  # Allows adding Answers from Question page

    def get_first_answer(self, obj):
        first_answer = obj.answer_set.first()  # Get the first related Answer object
        return first_answer.text if first_answer else "No answer"
    get_first_answer.short_description = 'First Answer'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # Assuming 'text' is a field in the Answer model
    list_display = ('id', 'question', 'text')
    # Search by question ID or answer text
    search_fields = ('question__id', 'text')
