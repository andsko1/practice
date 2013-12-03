# Create your views here.
import os
import time

from django.shortcuts import render_to_response
def home(request):
    return render_to_response('home.html')
def listing(request, path):
    base = '/var/log/'
    allfiles = os.listdir(base + path)
    files = []
    dirs = []
    for i in allfiles:
        fullpath = base + path + "/" + i
        if(os.path.isfile(fullpath)):
            files.append({"name": i, "size": str(os.path.getsize(fullpath))+' B', "lastmodtime": time.ctime(os.path.getmtime(fullpath))})
        elif(os.path.isdir(fullpath)):
            dirs.append({"name": i, "size": str(os.path.getsize(fullpath))+' B', "lastmodtime": time.ctime(os.path.getmtime(fullpath))})        
    return render_to_response('listing.html', {'directory': base + path, 'file_list': files, 'dir_list': dirs}) 
