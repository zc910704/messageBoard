from django.contrib import admin

from .models import Msg


class MsgAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'msg_text', 'msg_sender']

admin.site.register(Msg, MsgAdmin)