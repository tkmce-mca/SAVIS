from django.db import models

# Create your models here.
class upload(models.Model):

    Standard = models.CharField(max_length=60)
    #shirt_size = models.CharField(max_length=2, choices=STD)
    chapter=models.CharField(max_length=20)
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.CharField(max_length=10)
    upload_mal=models.FileField(upload_to='newapp/media/',max_length=2000, default="")
    upload_eng=models.FileField(upload_to='newapp/media/',max_length=2000, default="")
    upload_sci=models.FileField(upload_to='newapp/media/',max_length=2000, default="")


    def __str__(self):
        return self.Standard
"""
    name = models.CharField(max_length=500)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")
    fields = ["name", "filepath"]
"""


class questions(models.Model):

    Standard = models.CharField(max_length=60)
    #shirt_size = models.CharField(max_length=2, choices=STD)
    subject=models.CharField(max_length=20)
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.CharField(max_length=10)
    question1=models.CharField(max_length=200)
    question2=models.CharField(max_length=200)
    question3=models.CharField(max_length=200)
    question4=models.CharField(max_length=200)
    question5=models.CharField(max_length=200)

    objects=models.Manager()

    def __str__ (self):
        return self.Standard

class answers(models.Model):
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    ans5 = models.CharField(max_length=200)

    objects = models.Manager()

#objects = models.questions()
