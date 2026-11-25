from django.shortcuts import render, redirect
from django.views import View
from .models import Video
from .forms import VideoForm

class HomeView(View):
    def get(self, request):
        return render(
            request,
            'home.html',
        )
class VideoListView(View):
    def get(self, request):
        videos = Video.objects.all()
        return render(
            request,
            'videos.html',
            {
                'videos': videos,
            }
        )
class VideoCreateView(View):
    def get(self, request):
        form = VideoForm()
        return render(
            request,
            'create_video.html',
            {
                'form': form,
            }
        )
    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos')

