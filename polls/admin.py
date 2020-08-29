from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)