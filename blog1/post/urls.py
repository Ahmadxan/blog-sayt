from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-page'),
    # path('<int:pk>/detail/', views.PostDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/detail/', views.post_detail, name='blog-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-page'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update-page'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-page'),

]
