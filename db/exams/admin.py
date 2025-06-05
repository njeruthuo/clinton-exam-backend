from django.contrib import admin
# import nested_admin
from .models import Exam, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2  # Number of empty forms displayed

    # def get_queryset(self, request):
    #     return super().get_queryset(request).only("id", "text", "is_correct", "question")


# class QuestionInline(nested_admin.NestedStackedInline):
#     model = Question
#     extra = 1  # Number of empty forms displayed
#     inlines = [AnswerInline]  # Nest Answers inside Questions


# class ExamAdmin(nested_admin.NestedModelAdmin):
#     inlines = [QuestionInline]  # Nest Questions inside Exams

#     def get_inline_instances(self, request, obj=None):
#         if obj is None:
#             return []
#         return super().get_inline_instances(request, obj)


# admin.site.register(Exam, ExamAdmin)
# from django.contrib import admin
# from .models import Exam, Question, Answer


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'timeline']
    search_fields = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'exam']
    list_filter = ['exam']
    search_fields = ['question_text']
    inlines = [AnswerInline]


# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ['text', 'question', 'is_correct']
#     list_filter = ['question', 'is_correct']
#     search_fields = ['text']
