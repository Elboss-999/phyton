from django.urls import path
from .views import HomePageView,CategoryPageListView,NewsDetailView

urlpatterns = [
    path('',HomePageView.as_view(),name = 'home'),
    path('category/<slug:slug>', CategoryPageListView.as_view(), name='category_posts'),
    path('news_detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]