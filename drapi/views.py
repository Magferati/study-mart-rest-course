from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
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
    return HttpResponse(json_data,content_type = 'application.json')
 
 
 #model instance
def aiquest_inst(request, pk):
    #complex data
    ai = Aiquest.objects.get(id=pk)
    #python dect
    serializer = AiquestSerializer(ai)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json send to user
    return HttpResponse(json_data,content_type = 'application.json')

#DeSerializers.............it's not warking...

@csrf_exempt
def aiquest_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = AiquestSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'successfully insert data.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application.json')

        # এখানে invalid হলে error ফেরত দিবে (serializer এখানে আছে)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application.json')

    # POST না হলে এখানে যাবে
    #return JsonResponse({"error": "Only POST method allowed"}, status=400)
    
    if request.mehtod == 'PUT':
        json_data = request.body
        #convert stream to json
        stream = io.BytesIO(json_data)
        #convert python to stream
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(aiq,data=pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'successfully update data.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application.json')

        # এখানে invalid হলে error ফেরত দিবে (serializer এখানে আছে)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application.json')
    

    if request.method == 'DELETE':
        json_data = request.body
        # json to stream
        stream = io.BytesIO(json_data)
        # stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        aiq.delete()
        res = {'massage':'successfully deleted data'}
        #convart json data
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

