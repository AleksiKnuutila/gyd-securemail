from django.contrib import admin

from .models import PublicKey, KeyMaster, DataRequest

admin.site.register(PublicKey)
admin.site.register(KeyMaster)
admin.site.register(DataRequest)
