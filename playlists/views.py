from django.shortcuts import render
from django.views import generic

from .models import Title, Song

# Create your views here.
class TitleListView(generic.ListView):
    template_name = "playlists/index.html"
    model = Title
    context_object_name = "titles"

class TitleDetailView(generic.DetailView):
    template_name = "playlists/title_detail.html"
    model = Title
    pk_url_kwarg = "title_id"
    context_object_name = "title"

class TellMeView(generic.TemplateView):
    template_name = "playlists/tellme.html"
