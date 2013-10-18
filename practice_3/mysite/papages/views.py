# Create your views here.
import os

from django.shortcuts import render_to_response

def listing(request, path):
    base = '/var/log/'

    allfiles = os.listdir(base + path)

    return render_to_response('listing.html', {'directory': base + path, 'file_list': allfiles}) 
