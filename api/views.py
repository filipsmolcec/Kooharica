import json
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializer import *
from main.models import *
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    def post(self, request):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        username = body['username']
        password = body['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

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
    
    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        recipes = Recipe.objects.all()
        data = RecipeSerializer(recipes, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        recipe = self.get_object(pk)
        data = RecipeSerializer(recipe).data
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        recipe = self.get_object(pk)
        data = request.data
        serializer = RecipeSerializer(recipe, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogPostList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        data = BlogPostSerializer(blog_posts, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogPostDetail(APIView):
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        blog_post = self.get_object(pk)
        data = BlogPostSerializer(blog_post).data
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        blog_post = self.get_object(pk)
        data = request.data
        serializer = BlogPostSerializer(blog_post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog_post = self.get_object(pk)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)