from django.urls import path

from . import views

app_name = 'playlists'

urlpatterns = [
    path('', views.TitleListView.as_view(), name='index'),
    path('tellme/', views.TellMeView.as_view(), name='tellme'),
    path('<uuid:title_id>/', views.TitleDetailView.as_view(), name='title_detail'),
]
