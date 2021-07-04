from django.urls import path,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,userpost
urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('create/',PostCreateView.as_view(),name='create'),
    path('update/<int:pk>/',PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='delete'),
    path('posts/',userpost,name='userpost'),

    
]
