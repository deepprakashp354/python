from django.db import models
from django.utils import timezone # django class for current time
import datetime #python's class for delta method

#every table is the class
class Question(models.Model): #inheriting the properties of the model.Model class
	question_text = models.CharField(max_length = 150)	#column name,CharField() defines it as character field
	date_published = models.DateTimeField('date published')  # creates a date time field

	def when_published_date(self): # we can also define our own method
		return self.date_published >= (timezone.now() - datetime.timedelta(days = 1)) #datetime.timedelta() methods specifying the time interval of 1 day

	def __str__(self): #To get the object parameters, or to view the table
		return self.question_text + " created on " + str(self.date_published)

class Answer(models.Model):
	question = models.ForeignKey(Question)  #Foreign Key column
	answer_text = models.CharField(max_length = 150)
	no_of_votes = models.IntegerField(default = 0) #Integer type of field

	def __str__(self):
		return self.answer_text + "is the answer of question " + str(self.question_id) + "and has" + str(self.no_of_votes) + "votes"
#after modifying the models.py please migrate first