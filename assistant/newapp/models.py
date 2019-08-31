from django.db import models

# Create your models here.
class Tutorial(models.Model):
    tutorial_title=models.CharField(max_length=200)
    turorial_content=models.TextField()
    tutorial_published=models.DateTimeField("date published")

    def _str_(self):
        return self.tutorial_title

