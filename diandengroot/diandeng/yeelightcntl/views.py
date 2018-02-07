from django.shortcuts import render
from django.views.generic.base import View
import json
from yeelightcntl import YeelightWifiBulbLanCtrl
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse

# Create your views here.



@method_decorator(csrf_exempt, name='dispatch')
class CntlYeelightBulb(View):


    def post(self, request):
#        req_dict = json.loads(request.body)
#        token = req_dict["token"]
#        text = req_dict["text"]
#        trigger_word = req_dict["trigger_word"]

#if token == "aPQk7fNoQV507Ygnx3OxR4gfqwQGROdDCfA0cHeQruk=":
#        if trigger_word == "dingdan":
        YeelightWifiBulbLanCtrl.toggle_bulb(1)

        return HttpResponse("toggle bulb ok")

    def get(self, request):
        YeelightWifiBulbLanCtrl.toggle_bulb(1)

        return HttpResponse("toggle bulb ok")
