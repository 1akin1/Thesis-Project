from django.db import models
 
class Thesis(models.Model):  
    author = models.CharField(max_length=255)
    type = models.CharField(max_length=255)  
    abstract = models.CharField(max_length=5000)  
    university = models.CharField(max_length=255)  
    institute = models.CharField(max_length=255)  
    keyword = models.CharField(max_length=255, blank=True)  
    language = models.CharField(max_length=255)  
    subject = models.CharField(max_length=255)  
    supervisor = models.CharField(max_length=255)  
    cosupervisor = models.CharField(max_length=255, blank=True)
    date = models.DateField()  # Added missing 'date' field

    class Meta:  
        db_table = "thesis"  