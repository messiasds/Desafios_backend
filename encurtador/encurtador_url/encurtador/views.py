import random
import string
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# passos

# criar uma view para receber a requisicao POST com  url original
# devolver a url encurtada
# armazenar a nova url e url original
# criar endpoint para verificar a url solicitada
# retornar url original

class EncurtadorURL(APIView):

    def post(self, request):

        url = request.POST.get('url')
        dominio = request.META.get('HTTP_HOST')
        url_resposta = encurtar_url(url, dominio)

        return Response(url_resposta)

# mudar para utils
def encurtar_url(url, dominio=''):

    letras = string.ascii_letters
    numeros = string.digits
    caracteres = letras + numeros
    gerado = "".join(random.choice(caracteres) for letra in range(10))
    url_final = f"{dominio}/{gerado}" 
    return url_final
    





