from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)