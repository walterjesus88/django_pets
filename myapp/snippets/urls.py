from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include

urlpatterns = [
    path('snippets/', views.snippetList.as_view()),
    path('snippets/<int:pk>/', views.snippetDetail.as_view()),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)