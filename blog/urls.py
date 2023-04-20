from django.urls import path
from .views import PostListView
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from . import views

# Mapping for the urls
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]