from django.http import HttpResponse
from django.template import loader

from .forms import PublicKeyForm
from .models import PublicKey, KeyMaster, DataRequest

import pdb

def index(request):
    return HttpResponse("Hello, world. You're at the securemsg index.")

def genkey(request):
    template = loader.get_template('securemsg/genkey.html')
    context = {}
    return HttpResponse(template.render(context, request))

def addkey(request):
    template = loader.get_template('securemsg/addkey.html')
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PublicKeyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            # there must be a more idiomatic way to do this..
            new_key = PublicKey(public_key = request.POST['public_key'], email_address = request.POST['email_address'])
            new_key.save()
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/securemsg/addkey/')
    else:
        return HttpResponseRedirect('/securemsg/addkey/')


def datarequest(request,slug):
    datareq = DataRequest.objects.get(slug=slug)
    return HttpResponse(datareq.data_blob)