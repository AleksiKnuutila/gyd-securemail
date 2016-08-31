from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.template import loader

from .forms import PublicKeyForm
from .forms import DataRequestForm
from .models import PublicKey, KeyMaster, DataRequest
from .libs.mail import send_login_mail

import json

import pdb

def index(request):
    if request.method == 'POST':
        context = {}
        #keymaster = KeyMaster(email = request.POST['email_address'])
        #keymaster.save()
        #send_login_mail(keymaster.email, keymaster.confirmation_token)
        #return JsonResponse({'success':'True'})
        #return render(request, 'securemsg/index.html', context)
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
        keymaster = KeyMaster(email = request.POST['email_address'])
        keymaster.save()
        send_login_mail(keymaster.email, keymaster.confirmation_token)
        return JsonResponse({'success':'True'})
    else:
        return HttpResponseRedirect('/securemsg/addkey/')

def sendfile_index(request):
    template = loader.get_template('securemsg/sendfile_index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def json_get_publickey(request):
    email = request.GET['email_address']
    km = KeyMaster.objects.filter(email=email)[0]
    dict = {'email': km.email,'public_key': km.public_key}
    return HttpResponse(json.dumps(dict))

" depracated "
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

" this endpoint is for ajax post requests "
def json_addencrypted(request):
    km = KeyMaster.objects.filter(email=request.POST['email'])[0]
    dr = DataRequest(key_master=km,data_blob=request.POST['data_blob'])
    dr.save()
    return HttpResponse(json.dumps({'response': '200 cool beans'}))

def decrypt_index(request):
    #dr = DataRequest.objects.filter(slug=request.GET['slug'])[0]
    #context = {'data_blob':dr.data_blob}
    context = {}
    template = loader.get_template('securemsg/decrypt_index.html')
    return HttpResponse(template.render(context, request))

def json_get_datareq(request):
    dr = DataRequest.objects.filter(slug=request.GET['slug'])[0]
    dict = {'slug':dr.slug,'data_blob':dr.data_blob}
    return HttpResponse(json.dumps(dict))

def json_confirmemail(request):
    try:
        keymaster = KeyMaster.objects.get(confirmation_token=request.POST['confirmation_token'])
        keymaster.confirmed = True
        keymaster.save()
        return HttpResponse(json.dumps({'response': '200 cool beans'}))
    except KeyMaster.DoesNotExist:
        return HttpResponse(json.dumps({'response': '404 Not found'}))

def json_addkeymaster(request):
    keymaster = KeyMaster(email = request.POST['email'])
    keymaster.save()
    send_login_mail(keymaster.email, keymaster.confirmation_token)
    return HttpResponse(json.dumps({'response': '200 cool beans'}))


def json_addkey(request):
    keymaster = KeyMaster.objects.get(email = request.POST['email'])
    keymaster.public_key = request.POST['public_key']
    keymaster.save()
    return HttpResponse(json.dumps({'response': '200 cool beans'}))

def login(request, confirmation):
    try:
        keymaster = KeyMaster.objects.get(confirmation_token=confirmation)
        keymaster.confirmed = True
        keymaster.save()

    except KeyMaster.DoesNotExist:
        raise Http404("Not found")

    return HttpResponseRedirect('/securemsg/addkey.html')
