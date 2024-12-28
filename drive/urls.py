from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('folder/create/<int:parent_id>/', views.create_folder, name='create_folder'),
    path('folder/rename/<int:folder_id>/', views.rename_folder, name='rename_folder'),
    path('folder/delete/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('folder/list/<int:folder_id>/', views.folder_list, name='folder_list'),
]
