from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from SWENGS_HW1.yamod.models import Student, Building
from SWENGS_HW1.yamod.serializers import StudentSerializer, BuildingSerializer


## STUDENT API Calls
@api_view(["GET", "POST"])
def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(data=serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def student_adapt(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(data=serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



## BUILDING API Calls
@api_view(["GET", "POST"])
def building_list(request):
    if request.method == "GET":
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(data=serializer.data)

    elif request.method == "POST":
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def building_adapt(request, id):
    try:
        building = Building.objects.get(id=id)
    except Building.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BuildingSerializer(building)
        return Response(data=serializer.data)

    elif request.method == "PUT":
        serializer = BuildingSerializer(instance=building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
