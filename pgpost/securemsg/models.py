from __future__ import unicode_literals

from django.db import models
from django.utils.crypto import get_random_string

""" Old public key model, keep for now for backwards compatibility """
class PublicKey(models.Model):
    public_key = models.TextField()
    email_address = models.EmailField()

""" KeyMaster model, holds info on requester and their public key """
class KeyMaster(models.Model):
    email = models.EmailField()
    # email needs to be confirmed before the user can haz requests
    confirmation_token = models.CharField(max_length=32,db_index=True)
    confirmed = models.BooleanField(default=False)
    # the generated public key
    public_key = models.TextField()
    # reference for user to show which key has been used
    private_key_file = models.CharField(max_length=128)

# generate a random string to use as a slug for the request
# not really guaranteed to be unique but should be fine for now...
def randomString():
    return get_random_string(length=32)

""" DataRequest model, contains the encrypted file"""
class DataRequest(models.Model):
    # request owner
    key_master = models.ForeignKey(KeyMaster,on_delete=models.CASCADE)
    # encrypted data blob, should contain file metadata and file
    data_blob = models.TextField()
    # request identifier
    slug = models.SlugField(default=randomString)
