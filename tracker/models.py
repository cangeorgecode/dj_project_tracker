from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    link = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
