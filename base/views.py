from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from .models import  Task
from django.urls import  reverse_lazy
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
class TaskCreate(CreateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskUpdate(UpdateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Hello {request.user.username}'})




def login_page(request):
    return render(request, 'base/login_page.html')
