from django.db import models

# Create your models here.

class Join(models.Model):
    #email = models.EmailField(default='ABC@hmail.com')
    search_string = models.CharField(unique=True, max_length=1000, default='ABC')
    friend = models.ForeignKey("self", related_name='referral',\
				null=True, blank=True)
    ref_id = models.CharField(max_length=120, default='ABC')
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)
    
    def __unicode__(self):
        return "Hi %s" %(self.search_string)
    
    class Meta:
        unique_together = ("search_string", "ref_id",)
    