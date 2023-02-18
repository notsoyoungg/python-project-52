from django.urls import path
from django_filters.views import FilterView
from .filter import TaskFilter

from task_manager.tasks import views

urlpatterns = [
    path('', FilterView.as_view(filterset_class=TaskFilter), name='tasks_list'),
    # path('', views.TaskListView.as_view(), name='tasks_list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/', views.TaskCreationView.as_view(), name='create_task'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
