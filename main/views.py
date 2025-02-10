from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
# from django.views.generic import  DetailView, UpdateView, DeleteView, View
# from django.views.decorators.http import require_http_methods
# from .serialiser import TagSerializer, PostSerializer
# from .models import Tag, Topic, Post
# from rest_framework.views import APIView, Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import (DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly) 
# import rest_framework
# from .models import Todo
a = []

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def log_in(request):
    return render(request, 'main/log_in.html')

def theme1(request):
    return render(request, 'main/theme1.html')

def theme2(request):
    return render(request, 'main/theme2.html')

def theme3(request):
    return render(request, 'main/theme3.html')

def test1(request):
    return render(request, 'main/test1.html')

def test2(request):
    return render(request, 'main/test2.html')

def test3(request):
    return render(request, 'main/test3.html')

def section(request):
    return render(request, 'main/section.html')

def info(request):
    return render(request, 'main/info.html')
# class TagViewSet(ModelViewSet):
#     serializer_class = TagSerializer
#     queryset = Tag.objects.all()
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# class TopicViewSet(ModelViewSet):
#     serializer_class = TopicSerializer
#     queryset = Topic.objects.all()
#     http_method_names = ['get']
#     permission_classes = [IsAccountAdminOrReadOnly]


# class PostViewSet(ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     permission_classes = [ IsAuthenticatedOrReadOnly]

    