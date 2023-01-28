from django.shortcuts import render
from django.http import HttpResponse
from .sms import envia_sms
from .models import Contato


def home(request):
    return HttpResponse('teste')


def envia_smss(request):
    contatos = Contato.objects.all()
    for contato in contatos:
        envia_sms(contato.celular)
    return HttpResponse('SOCIEDADE')

