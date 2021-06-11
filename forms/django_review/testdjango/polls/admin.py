from django.contrib import admin
from .models import Question, Choice
#copying template from 'C:\Users\LCM\pythonprojects\django\env\lib\python3.6\site-packages\django\contrib\admin\templates\admin'

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
# make this more compact -> TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    # grouping the sets
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                            'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # that extra filter tab on the right that seems quite meaningless in some cases
    search_fields = ['question_text'] # adds the search box at the top of the list




admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice) # on the separate screen
