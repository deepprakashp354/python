from django.contrib import admin
from src.models import Question, Answer

# Register your models here.

#class AnswerInLine(admin.StackedInline): #Stacked format
				#or
class AnswerInLine(admin.TabularInline): #Tabular format
	model = Answer  #model means database, it is taking the Answer database
	extra = 1		#how many fields of answer should be shown

class QuestionDisplay(admin.ModelAdmin):
	#fields = ['date_published', 'question_text'] #getting the fields
	fieldsets = [			#fieldsets is the predefined parameter
	("Question Info",{'fields' : ['question_text']}),
	("Date Info", {'fields' : ['date_published']})
	]
	inlines = [AnswerInLine] #inlines is the predefined parameter
	search_fields = ['question_text'] #Adds the search field


admin.site.register(Question, QuestionDisplay)
#admin.site.register(Answer)