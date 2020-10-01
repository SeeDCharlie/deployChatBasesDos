from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from chat.models import *
from chat.serializers import *
from rest_framework import permissions
from chat.permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate, login, logout
# Create your views here.
"""
{
    "email": "hellocarloscastillo@gmail.com",
    "password": "seed777"
}
"""


def index(request):
    return HttpResponse('<h1>alv!! chat de la shit<h1/>')

class api_cStates(APIView):

    permission_classes = [permissions.IsAuthenticated]
                      #IsOwnerOrReadOnly]

    def get(self, request):
        print('getestados : ')
        states = c_states.objects.all()
        print('getestados : ', states)
        try :
            sz = szc_states(states, many = True)
            print('get estados : ', sz.data)
            return Response(sz.data)
        except Exception as error :
            print('error states : ', error)
            return Response({'erro' : error})
    


class api_login(APIView):

    def get(self, request):
        return Response({'email':'example@example.com', 'password':'secretPassword'})

    def post(self, request):
        email = request.data['email']
        passw = request.data['password']
        user = authenticate(email = email, password = passw)
        if user is not None:
            login(request, user)
            user = sz_users(user)
            return Response({'is_login': True, 'user' : user.data})
        else:
            return Response({'is_login': False, 'user' : None})


def logout_view(request):
    logout(request) 
    return redirect('admin')





