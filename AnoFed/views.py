from django.shortcuts import render
from django.http import HttpResponse
import json
from firstWEB.models import Test, Tokenizerdict
import jieba
import jieba.posseg as pseg

# Create your views here.
def postokenhtml(requests):
    context = {}
    context["vueData"] = "{{ section.text }}"
    return render(requests,'POSTokenizer.html',context)

def addProj(requests):
    test1 = Test(name=requests.GET.get('name'))
    test1.save()
    return HttpResponse("success")

def addToken(requests):
    newtoken = Tokenizerdict(tokenizer=requests.GET.get('token'),
        freq=requests.GET.get('freq'),
        pos=requests.GET.get('pos'),
        pid=int(requests.GET.get('pid')))
    newtoken.save()
    return HttpResponse("success")

def deleteToken(requests):
    Tokenizerdict.objects.filter(tokenizer=requests.GET.get('token'),
        pid=int(requests.GET.get('pid'))).delete()
    return HttpResponse("success")

def selectProj(requests):
    queryrsts = Test.objects.all()
    context = {}
    context['queryrsts'] = queryrsts
    return render(requests,'projList.html',context)

def selectToken(requests):
    queryrsts = Tokenizerdict.objects.filter(pid=int(requests.GET.get('pid'))) 
    context = {}
    context['queryrsts'] = queryrsts
    return render(requests,'tokenForm.html',context)

def tokenfeedbackhtml(requests):
    context = {}
    return render(requests,'TokenFeedback.html',context)

def jiebaToken(requests):
    words = pseg.cut(requests.GET.get('str'))
    token = []
    for word, flag in words:
        token.append([word,flag])
    context = {}
    context["token"] = token
    return render(requests,'messageBox.html',context)
