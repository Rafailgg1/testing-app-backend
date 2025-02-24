from django.contrib import admin
from .models import Test, Question, Answer


class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'background_image'] 
    
    
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    fields = ['text', 'is_correct', 'result_message', 'result_image', 'redirect_to']
    fk_name = 'question'  
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['text', 'test', 'redirect_to']
    list_filter = ['test']
    search_fields = ['text']
    autocomplete_fields = ['redirect_to']
    

admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)


