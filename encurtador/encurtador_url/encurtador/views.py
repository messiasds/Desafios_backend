import random
import string
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from rest_framework.renderers import JSONRenderer

class RedirecionarURL(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, url_curta):

        ''' obtem a url original a partir da url encurtada '''

        url_curta = url_curta.replace('/','')

        try:
            url_original = models.URL.objects.get(new_url__exact=url_curta)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        dados = serializers.OriginalURlSerializer(url_original).data

        return Response(dados, status= status.HTTP_200_OK)


class EncurtadorURL(APIView):

    ''' 
        encurta a URL, salva no Banco e retorna a o endpoint do recurso 
        no IP atual do servidor '''

    renderer_classes = [JSONRenderer]

    def post(self, request):

        url_original = request.POST.get('url')
        dominio = request.META.get('HTTP_HOST')

        url_curta = encurtar_url(url_original)
        obj = salvar_url(url_original, url_curta)

        dados = serializers.NewURLSerializer(obj).data
        dados['newUrl'] = f"{dominio}/{url_curta}"

        return Response(dados, status.HTTP_201_CREATED)


def encurtar_url(url, dominio=''):

    letras = string.ascii_letters
    numeros = string.digits
    caracteres = letras + numeros
    gerado = "".join(random.choice(caracteres) for letra in range(10))
    url_final = gerado
    return url_final

def salvar_url(original, nova):

    url_obj = models.URL(
        original_url = original,
        new_url = nova,
    )

    url_obj.save()
    return url_obj



