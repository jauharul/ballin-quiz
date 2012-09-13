from quiz.models import *
from django.contrib import admin

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Quiz information', {'fields': ['category', 'description',], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]
    list_display = ('title', 'created', )
    list_per_page = 10  # default 100
    search_fields = ('title', )
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user.username
        obj.save()

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Score)
