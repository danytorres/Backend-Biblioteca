from django.db import models
from dispositions.models import Disposition
from affair.models import Affair

# Model para los documentos subidos en elastic search
class Biblioteca(models.Model):
    dispositionTitle = models.CharField(max_length=155, blank=True)
    date = models.CharField(max_length=155, blank=True)
    volume = models.CharField(max_length=155, blank=True)
    pageNumbers = models.CharField(max_length=155, blank=True)
    legislationTranscriptOriginal = models.FileField(blank=True, null=False)
    legislationTranscriptCopy = models.TextField(blank=True)
    place = models.CharField(max_length=155, blank=True)
    dispositionNumber = models.IntegerField(blank=True)
    dispositionTypeId = models.ForeignKey(
        Disposition, models.SET_NULL, blank=True, null=True
    )
    affairId = models.ForeignKey(
        Affair, on_delete=models.SET_NULL, blank=True, null=True
    )
