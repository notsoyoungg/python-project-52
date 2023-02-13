from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
    path('create/', views.RegistrationView.as_view(), name='register'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]
