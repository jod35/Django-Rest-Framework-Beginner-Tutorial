from django.shortcuts import render
from . import serializers
from .models import Todo
from rest_framework import generics,status
from django.http import HttpRequest
from rest_framework.response import Response

# Create your views here.

class TodosView(generics.GenericAPIView):

    serializer_class=serializers.TodoSerializer
    queryset=Todo.objects.all()

    def get(self,request:HttpRequest):
        """get all todos """
        

        todos=Todo.objects.all()


        serializer=self.serializer_class(instance=todos,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)



    
    def post(self,request:HttpRequest):
        """Create a todo """
        
        data=request.data


        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED,data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors)


class TodoView(generics.GenericAPIView):
    serializer_class=serializers.TodoSerializer

    def get(self,request:HttpRequest,id):
        """Get a todo by id """
        todo=Todo.objects.get(pk=id)

        serializer=self.serializer_class(instance=todo)

        return Response(status=status.HTTP_200_OK,data=serializer.data)



    def put(self,request:HttpRequest,id):
        """Update a todo by id"""
        todo=Todo.objects.get(pk=id)

        if todo is not None:
            serializer=self.serializer_class(instance=todo,data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)

            else:
                return Response(data={"message":"Resource Not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(data=serializer.errors,
                    status=status.HTTP_404_NOT_FOUND
                )

    def delete(self,request:HttpRequest,id):
        """Delete a to by id"""

        todo_to_delete=Todo.objects.get(pk=id)

        todo_to_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



    def patch(self,request:HttpRequest,id):
        """Updating status of a todo"""

        todo_to_update=Todo.objects.get(pk=id)

        serializer=self.serializer_class(instance=todo_to_update,data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(status=HTTP_400_BAD_REQUEST,data=serializer.errors)

        


