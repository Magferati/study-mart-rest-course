from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.
#Queryset
def aiquest_info(request):
    #complex data
    ai = Aiquest.objects.all()
    #python dect
    serializer = AiquestSerializer(ai, many=True)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json send to user
    return HttpResponse(json_data,content_type = 'application/json')
 
 
 #model instance
def aiquest_inst(request, pk):
    #complex data
    ai = Aiquest.objects.get(id=pk)
    #python dect
    serializer = AiquestSerializer(ai)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json send to user
    return HttpResponse(json_data,content_type = 'application/json')

#DeSerializers................
@csrf_exempt
def aiquest_create(request):
    if request.methode == "POST":
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python convert
        python_data = JSONParser().parse(stream)
        #python to complex
        serializer = AiquestSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'masg':'successfully insert data.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application.json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application.json')