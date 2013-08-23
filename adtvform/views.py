from django.http import HttpResponse
from django.shortcuts import render
from models import Search, SearchForm

import os

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            valor = Search()
            
            valor.sdata = request.POST['sdata']
            valor.sdate = request.POST['sdate']
            
            valor.save()
            
            return render(request, 'form.html', { 
                'form': form, 
            })
    else:
        form = SearchForm() # An unbound form

    return render(request, 'form.html', {
        'form': form,
    })