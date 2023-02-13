from django.urls import path

from task_manager.labels import views

urlpatterns = [
    path('', views.LabelListView.as_view(), name='label_list'),
    path('create/', views.LabelCreationView.as_view(), name='create_label'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label_delete'),
]
