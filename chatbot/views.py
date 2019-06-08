import json
from django.shortcuts import render
# from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings


class 챗뷰(TemplateView):
  template_name = 'home.html'

chatterbot = ChatBot(**settings.CHATTERBOT)

@api_view(['POST'])
def chatAPI(request):

  # input_data = json.loads(request.data.decode('utf-8'))
  input_data = request.data

  if 'text' not in input_data:
      return Response({
          'text': [
              '"text":"xxxxxxxxx"를 입력해 주세요.'
          ]
      }, status=400)

  response = chatterbot.get_response(input_data)
  response_data = response.serialize()

  return Response(response_data, status=200)