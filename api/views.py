from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from api.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import User

class UserList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = User.objects.all()
        data = UserSerializer(users, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)