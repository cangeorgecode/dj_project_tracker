from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    link = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def datecreated(self):
        return self.date_created.strftime('%B %d %Y')
