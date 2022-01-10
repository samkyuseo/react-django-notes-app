from django.db import models

# Create your models here.
class Note(models.Model): 
    body = models.TextField(null=True, blank=True) # can be empty in db and can submit a form with nth in it
    updated = models.DateTimeField(auto_now=True) # on every save get current time
    created = models.DateTimeField(auto_now_add=True) # only set time on add (aka first time)

    def __str__(self):
        return self.body[0:50] # only return the first 50 chars so its neater looking