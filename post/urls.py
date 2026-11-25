from django.urls import path
from .views import HomeView, VideoListView, VideoCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('video/', VideoListView.as_view(), name='videos'),
    path('video/create/', VideoCreateView.as_view(), name='create_video'),
    
]
