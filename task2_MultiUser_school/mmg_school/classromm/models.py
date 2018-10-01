from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Subject(models.Model):
    name = models.CharField(max_length=200)
    color= models.CharField(max_length=7,default ='#007bff')
    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner   = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='quizes')
    name    = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject  ,on_delete=models.CASCADE ,related_name='quizes')

    def __str__(self):
        return self.name

class Quesstion(models.Model):
    quiz = models.ForeignKey(Quiz ,on_delete=models.CASCADE,related_name='questions')
    text = models.CharField('Question',max_length=200)

    def __str__(self):
        return self.text
class Answer(models.Model):
    question = models.ForeignKey(Quesstion,on_delete=models.CASCADE,related_name='answers')
    text     = models.CharField('Answer' , max_length=200)
    is_correct = models.BooleanField('Corect Answer',default=False)

    def __str__(self):
        return self.text

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    quizzes = models.ManyToManyField(Quiz,through='TakenQuiz')
    interest = models.ManyToManyField(Subject ,related_name='interested_student')

    def __str__(self):
        return self.user.username

class TakenQuiz(models.Model):
    student = models.ForeignKey(Student ,on_delete=models.CASCADE,related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz ,on_delete=models.CASCADE,related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class StudentAnswer(models.Model):
    student =models.ForeignKey(Student ,on_delete=models.CASCADE ,related_name='quiz_answers')
    answer =models.ForeignKey(Answer ,on_delete=models.CASCADE ,related_name='+')
