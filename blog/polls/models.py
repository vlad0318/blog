from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	date_pub = models.DateTimeField("date published")
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.date_pub >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	questions = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text