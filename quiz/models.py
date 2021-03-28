from django.db import models

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

    def __str__(self):
        return self.question_title
