from django.shortcuts import render
import requests
import bs4
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
import time
from . import engine

@api_view(['GET','POST'])
def temperature(request):
    if request.method == 'POST':
        city=JSONParser().parse(request)
        data=city["city_name"]
        print(data)
        temp_value=engine.tempFunc(data)
        print(temp_value)
        json_data={"value":temp_value}
        return JsonResponse(json_data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT'])
def geti(request):
    if request.method=='GET':
        value=engine.tempFunc("Meerut")
        json_data={"var":value}
        with open('jsonfiles/temp.json') as f:
            data12=json.load(f)
        return Response(data12, status=status.HTTP_201_CREATED)
        #return JsonResponse(data12,status=status.HTTP_201_CREATED)