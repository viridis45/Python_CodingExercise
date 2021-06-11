import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # display the content itself when called externally
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean = True,
        ordering = 'pub_date',
        description = 'Published recently?',
    )
    def was_published_recently(self): # sorting with method is not supported in admin page
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Foreign Key automatically converts into select box in admin. add another button too.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


