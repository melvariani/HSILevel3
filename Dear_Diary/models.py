from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Entry(models.Model): #tabel namanya entry
    #membuat 2 kolom di database
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Entry #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural='entries'
    
    
    