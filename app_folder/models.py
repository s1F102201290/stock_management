from django.db import models

# Create your models here.
class SampleDB(models.Model):
    class Meta:
        db_table = 'sample_table' 
        verbose_name_plural = 'sample_table'
    sample1 = models.IntegerField('sample1', null=True, blank=True) 
    sample2 = models.CharField('sample2', max_length=255, null=True, blank=True) 