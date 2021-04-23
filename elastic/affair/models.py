from django.db import models

# Create your models here.
class Affair(models.Model):
    id = models.AutoField(verbose_name='ID', auto_created=True, primary_key=True)
    affair = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.affair
