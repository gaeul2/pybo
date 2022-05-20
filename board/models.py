from django.db import models


# Create your models here.
class Question(models.Model):
    class Meta:
        db_table = 'question'
        app_label= 'board'

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    class Meta:
        db_table = 'answer'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
