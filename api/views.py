from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
from rest_framework.parsers import JSONParser

# Create your views here.
# users/
class UserList(APIView):

    def post(self,request,format=None): # 사용자 추가
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def get(self, request,format=None): #모든 사용자 조회
        queryset=User.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return Response(serializer.data)

#users/pk/
class UserDetail(APIView):

    # 특정 사용자 조회
    def get(self,request,pk):
        user=User.objects.get(pk=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)

    # 특정 사용자정보 수정
    def put(self,request,pk,format=None):
        user=User.objects.get(pk=pk)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 특정 사용자 제거
    def delete(self,request,pk,format=None):
        user=User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


