from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.forms import ModelForm

import datetime

class Search(models.Model):
    sdata = models.CharField(max_length=10)
    sdate = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        verbose_name = _("Search")
        verbose_name_plural = _("Searches")
    
class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ['sdata', 'sdate']