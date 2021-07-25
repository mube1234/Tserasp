from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from ..models import Schedule
from rest_framework.decorators import api_view
from .serializers import ScheduleSerializer


@api_view(['GET', 'POST'])
def schedule_list(request):
    if request.method == 'GET':
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # status 201 shows it is a created status
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def schedule_detail(request,pk):
    schedule=Schedule.objects.get(id=pk)
    Serializer=ScheduleSerializer(schedule,many=False)
    return Response(Serializer.data)