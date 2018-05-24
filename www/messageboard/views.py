
import datetime
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import generic
from messageboard.models import Msg
import pytz
import pdb


def msgboardIndex(request):
    latest_msg_list = Msg.objects.order_by('-pub_date')
    if request.method == "POST":
        msg_sender_ip = request.META['REMOTE_ADDR']
        msg_sender = request.POST['msg_sender']
        if msg_sender is not None:
            pass
        else:
            msg_sender = msg_sender_ip
        msg_text = request.POST['msg_text']
        pub_date = datetime.datetime.now(pytz.utc)
        # pdb.set_trace()
        msg = Msg(msg_text = msg_text, msg_sender = msg_sender, pub_date = pub_date)
        msg.save()
        # latest_msg_list.append(Msg(msg_sender, msg_text, pub_date))
    elif request.method == "GET":
        pass
    content = {'latest_msg_list':latest_msg_list}
    return render(request, 'messageboard/msg.html', content)
