from django.shortcuts import render, get_object_or_404
from .serializers import Person, PersonSerializer
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])

def personview(request):
    
    if request.method=='GET':
        pk = request.query_params.get('id')

        if pk is not None:
            obj = Person.objects.get(id=pk)
            serializer = PersonSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        pk = request.query_params.get('id')
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        pk = request.query_params.get('id')
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pk = request.query_params.get('id')
        obj = get_object_or_404(Person, id=pk)
        obj.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    



