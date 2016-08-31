from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader

from .forms import PublicKeyForm
from .forms import DataRequestForm
from .models import PublicKey, KeyMaster, DataRequest
from .libs.mail import send_login_mail

import pdb

def index(request):
    if request.method == 'POST':
        context = {}
        keymaster = KeyMaster(email = request.POST['email_address'])
        keymaster.save()
        send_login_mail(keymaster.email, keymaster.confirmation_token)
        return render(request, 'securemsg/index.html', context)
    else:
        context = {}
        return render(request, 'securemsg/index.html', context)

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

def sendfile_index(request):
    template = loader.get_template('securemsg/sendfile_index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def encryptfile(request):
    email = request.POST['email_address']
    km = KeyMaster.objects.filter(email=email)
    public_key = km[0].public_key
    template = loader.get_template('securemsg/encryptfile.html')
    form = DataRequestForm()
    context = {'public_key':public_key,'form':form,'email':email}
    return HttpResponse(template.render(context, request))

def addencrypted(request):
    pdb.set_trace()
    km = KeyMaster.objects.filter(email=request.POST['email'])[0]
    dr = DataRequest(key_master=km,data_blob=request.POST['data_blob'])
    dr.save()
    template = loader.get_template('securemsg/addkey.html')
    context = {}

def login(request, confirmation):
    try:
        keymaster = KeyMaster.objects.get(confirmation_token=confirmation)
        keymaster.confirmed = True
        keymaster.save()

    except KeyMaster.DoesNotExist:
        raise Http404("Not found")

    return HttpResponseRedirect('/securemsg/addkey.html')
