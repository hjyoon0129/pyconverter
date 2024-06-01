from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='humor_author_questions')
    voter = models.ManyToManyField(User, related_name='humor_voter_questions')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='question_images', null=True, blank=True)


    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='humor_author_answer')
    voter = models.ManyToManyField(User, related_name='humor_voter_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
