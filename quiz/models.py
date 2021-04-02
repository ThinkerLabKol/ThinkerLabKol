from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_title = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_ans = models.TextField()
    max_marks = models.IntegerField()

    def __str__(self):
        return self.question_title

class Record(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_ans = models.TextField()
    user_ans = models.TextField(default=' ', blank=True, null=True)

    def __str__(self):
        return self.question

class Scorecard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    obtained_marks = models.IntegerField()
    correct_ans = models.IntegerField()
    wrong_ans = models.IntegerField()

    def __str__(self):
        return self.user.username