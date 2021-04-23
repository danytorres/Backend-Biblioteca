from django.db import models

# Create your models here.
class Disposition(models.Model):
    id = models.AutoField(verbose_name='ID', auto_created=True, primary_key=True)
    dispositionType = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.dispositionType

