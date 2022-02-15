from django.shortcuts import render
from django.views import View
from .models import Person
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class PersonView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if (id > 0):
            people = list(Person.objects.filter(id=id).values())
            if len(people) > 0:
                person = people[0]
                data = {'message': "Success" ,"people": person}
            else:
                data = {'message': "Person not found."}
            return JsonResponse(data)
        else:
            people = list(Person.objects.values())
            if len(people) > 0:
                data = {'message': "Success", 'people': people}
            else:
                data = {"message": "People not found."}
            return JsonResponse(data)

    def post(self, request):
        jsdata = json.loads(request.body)
        Person.objects.create(document_type=jsdata['document_type'], document_num=jsdata['document_num'], 
                names=jsdata['names'], lastnames=jsdata['lastnames'], hobbie=jsdata['hobbie'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jsdata = json.loads(request.body)
        people = list(Person.objects.filter(id=id).values())
        if len(people) > 0:
            person = Person.objects.get(id=id)
            person.document_type = jsdata['document_type']
            person.document_num = jsdata['document_num']
            person.names = jsdata['names']
            person.lastnames = jsdata['lastnames']
            person.hobbie = jsdata['hobbie']
            person.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Person not found."}
        return JsonResponse(data)


    def delete(self, request, id):
        people = list(Person.objects.filter(id=id).values())
        if len(people) > 0:
            Person.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Person not found."}
        return JsonResponse(data)

