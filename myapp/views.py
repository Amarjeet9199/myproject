# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Myapp
from . serializers import MyappSerializer

class MyappListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Myapp.objects.filter(user = request.user.id)
        serializer = MyappSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'id': request.data.get('id'),
            'firstname': request.data.get('firstname'), 
            'lastname': request.data.get('lastname'), 
            'companyname': request.data.get('companyname'), 
            'city': request.data.get('city'), 
            'state': request.data.get('state'), 
            'zip': request.data.get('zip'),
            'mail': request.data.get('mail'), 
            'web': request.data.get('web'), 
            'age': request.data.get('age'), 
            'user': request.user.id
        }
        serializer = MyappSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'id': request.data.get('id'),
            'firstname': request.data.get('firstname'), 
            'lastname': request.data.get('lastname'), 
            'companyname': request.data.get('companyname'), 
            'city': request.data.get('city'), 
            'state': request.data.get('state'), 
            'zip': request.data.get('zip'),
            'mail': request.data.get('mail'), 
            'web': request.data.get('web'), 
            'age': request.data.get('age'), 
            'user': request.user.id
        }
        serializer = MyappSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

        