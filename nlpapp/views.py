from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .modules.questions.interface import QuestionInterface as Interface
# Create your views here.

try:
    q
except NameError:
    q = Interface()

def index(req):
    return render(req, 'index.html', {})

def get_sent(req):
    text = req.GET['text']
    opt = req.GET['option']
    ret = {
        'text': '',
        'err': False
    }

    if opt in q.options:
        ret['text'] = q.get_text(text, opt)
    else:
        ret['err'] = True
    
    return JsonResponse(ret)

def get_options(req):
    return JsonResponse({
        'options': q.options
    })