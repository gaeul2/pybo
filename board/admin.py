from django.contrib import admin
from .models import Question,Answer

# Register your models here.
class Question_search_of_subject(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, Question_search_of_subject)
admin.site.register(Answer)