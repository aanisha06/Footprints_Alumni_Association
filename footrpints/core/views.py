from django.shortcuts import render
from django.http import JsonResponse
from .models import OfficialAlumni
from .serializers import AlumniSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def alumni_list(request):

    if request.method =='GET':
        alumni_record = OfficialAlumni.objects.filter()
        serializer= AlumniSerializer(alumni_record, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        verify_data= request.data
        try:
            reg= verify_data['regno']
            print("------------test", reg)
            record = OfficialAlumni.objects.filter(regno=reg)
            serializer = AlumniSerializer(data=request.data)
            if serializer.is_valid():
                    # serializer.save()
                    return Response(serializer.data)
            else:
                print(serializer.data)
                return Response("oops")
        except Exception as e:
            print(e)
            return Response("ooo")
             
