import mimetypes
from wsgiref.util import FileWrapper

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.
def index(request):
    FILES = []
    for filename in os.listdir(settings.HOME_PATH):
        if filename[0] != ".":
            if os.path.isdir(settings.HOME_PATH+"/"+filename):
                FILES.append([filename, "red"])
            elif os.path.isfile(settings.HOME_PATH+"/"+filename):
                FILES.append([filename, "blue"])
    FILES.sort()
    return render(request, "sindex.html", {"path":str(settings.HOME_PATH), "files":FILES})

def folder(request):
    FOLDER = request.GET['folder']
    if os.path.isdir(FOLDER):
        FILES = []
        for filename in os.listdir(FOLDER):
            if filename[0] != ".":
                if os.path.isdir(FOLDER+"/"+filename):
                    FILES.append([filename, "red"])
                elif os.path.isfile(FOLDER+"/"+filename):
                    FILES.append([filename, "blue"])
        FILES.sort()
        pathq = FOLDER.split("/")

        #for i in range(0, 3):
        pathq.remove(pathq[0])

        l = []
        v = str(settings.HOME_PATH)[:-1]

        for o in pathq:
            v += "/" + o
            l.append(v)

        path = []
        for o in range(0, len(pathq)):
            path.append([pathq[o], l[o]])

        return render(request, "folder.html", {"folder":FOLDER, "files":FILES, "pathq": path})

    if os.path.isfile(FOLDER):
        file_wrapper = FileWrapper(open(FOLDER, 'rb'))
        file_mimetype = mimetypes.guess_type(FOLDER)
        response = HttpResponse(file_wrapper, content_type=file_mimetype)
        response['X-Sendfile'] = FOLDER
        response['Content-Length'] = os.stat(FOLDER).st_size
        file_name = FOLDER.split("/")[len(FOLDER.split("/"))-1]
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    else:
        return HttpResponse("Neplatná cesta")

def search(request):
    pass

def file(request):
    pass
