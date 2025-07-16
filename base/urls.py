from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, HelloView, login_page

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('login/', login_page, name='login'),
]
