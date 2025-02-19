from django.shortcuts import render, redirect, get_object_or_404
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
from django.db import models
from rest_framework import viewsets
from .models import  Test, Question, Answer
from rest_framework import serializers
from django.shortcuts import render, redirect
from .models import Test
from .serializers import TestSerializer
from django.urls import reverse



def views_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'main/test_template.html', {'test': test})

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
def start_test(request, test_id):
    request.session['test_id'] = test_id
    request.session['question_index'] = 1  # Начинаем с первого вопроса
    request.session['score'] = 0
    return redirect('question', test_id=test_id, question_number=1)  # Передаем оба аргумента

def question(request, test_id, question_number):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all().order_by('id')
    
    if question_number > len(questions):
        return redirect('results')
    
    current_question = questions[question_number - 1]
    
    if request.method == 'POST':
        selected_answer_id = request.POST.get('answer')
        if selected_answer_id:
            answer = get_object_or_404(Answer, id=selected_answer_id)
            if answer.is_correct:
                request.session['score'] += 1
        request.session['question_index'] += 1
        return redirect('question', test_id=test_id, question_number=question_number + 1)
    
    return render(request, 'main/question.html', {
        'question': current_question,
        'question_number': question_number,
        'total_questions': len(questions),
        'test_id': test_id,  # Передаем test_id в шаблон
    })

def results(request):
    score = request.session.get('score', 0)
    total = Test.objects.get(id=request.session['test_id']).questions.count()
    return render(request, 'main/results.html', {'score': score, 'total': total})
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

    