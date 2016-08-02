from django.shortcuts import render

from .models import Performer, Song

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'songs/song_list.html')

def song_detail(request, pk):
  song = get_object_or_404(Song, pk=pk)
  return render(request, 'song/song_detail.html')

def performer_detail(request, song_pk, performer_pk):
  performer = get_object_or_404(Performer, song_id=pk, pk=performer_pk)
  return render(request, 'songs/performer_detail.html', {performer: performer})


