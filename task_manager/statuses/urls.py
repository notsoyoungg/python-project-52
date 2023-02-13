from django.urls import path

from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesListView.as_view(), name='statuses_list'),
    path('create/', views.StatuseCreationView.as_view(), name='create_status'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
]
