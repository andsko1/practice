# Create your views here.
import os

from django.shortcuts import render_to_response

def listing(request, path):
    base = '/var/log/'

    allfiles = os.listdir(base + path)
    files = []
    dirs = []
    for i in allfiles:
        fullpath = base + path + "/" + i
        if(os.path.isfile(fullpath)):
            files.append(i)
        elif(os.path.isdir(fullpath)):
            dirs.append(i)       
    return render_to_response('listing.html', {'directory': base + path, 'file_list': files, 'dir_list': dirs}) 
