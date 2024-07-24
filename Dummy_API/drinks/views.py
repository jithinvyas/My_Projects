from django.shortcuts import render
# from django.http import JsonResponse, request
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.         --> Creating end points (serializers)

@api_view(['GET','POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()   # getting all the drinks
        serializer = DrinkSerializer(drinks, many=True) # Serialize them
        return Response(serializer.data)
    
    elif request.method == 'POST':       ## Adding a drink to the db, (deserialize)
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Ensure a response is always returned
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id) # access drink object
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':  # Updating
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)