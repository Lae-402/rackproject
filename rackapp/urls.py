from django.urls import path
from . import views

app_name = "rackapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowToView.as_view(), name='howto'),
    path('rack', views.RackView.as_view(), name='rack'),
    path("register/artist", views.RegisterArtistView.as_view(), name="register_artist"),
    path("register/artist_done/", views.ArtistSuccessView.as_view(), name="artist_done"),
    path("register/", views.AddRackView.as_view(), name="register"),
    path("register_done/", views.RegisterSuccessView.as_view(), name="register_done"),
    path("rack/<int:pk>/detail", views.DetailView.as_view(), name="detail"),
    path("rack/<int:pk>/delete", views.RackDeleteView.as_view(), name="delete"),
    path("rack/media/<int:media>", views.MediaView.as_view(), name="media"),
    path("rack/artist/<int:artist>", views.ArtistView.as_view(), name="artist"),
]