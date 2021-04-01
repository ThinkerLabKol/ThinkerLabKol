from django.contrib import admin
from .models import Quiz, Question, Record, Scorecard

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Record)
admin.site.register(Scorecard)