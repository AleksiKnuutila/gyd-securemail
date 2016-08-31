from django.http import HttpResponse, HttpResponseRedirect
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
        send_login_mail(request.POST['email_address'], "foo")
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
    pdb.set_trace()
    public_key = km[0].public_key
    template = loader.get_template('securemsg/encryptfile.html')
    form = DataRequestForm()
    context = {'public_key':public_key,'form':form,'email':email}
    return HttpResponse(template.render(context, request))

def addencrypted(request):
    km = KeyMaster.objects.filter(email=request.POST['email'])[0]
    dr = DataRequest(key_master=km,data_blob=request.POST['data_blob'])
    dr.save()
    template = loader.get_template('securemsg/addencrypted.html')
    context = {}
    return HttpResponse(template.render(context, request))

def decrypt_index(request):
    dr = DataRequest.objects.filter(slug=request.GET['slug'])[0]
    context = {'data_blob':dr.data_blob}
    template = loader.get_template('securemsg/decrypt_index.html')
    return HttpResponse(template.render(context, request))
