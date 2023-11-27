from django.urls import path
from . import views

app_name = "rackapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rack', views.RackView.as_view(), name='rack'),
    path("post/", views.CreatePhotoView.as_view(), name="register"),
    path("post_done/", views.RegisterSuccessView.as_view(), name="register_done"),
    path("rack/<int:pk>/detail", views.DetailView.as_view(), name="detail"),
    path("rack/<int:pk>/delete", views.DeleteView.as_view(), name="delete"),
    path("rack/media/<int:media>", views.MediaView.as_view(), name="media"),
    path("rack/artist/<int:artist>", views.ArtistView.as_view(), name="artist"),
]

# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("post/", views.CreatePhotoView.as_view(), name="post"),
#     path("post_done/", views.PostSuccessView.as_view(), name="post_done"),
#     path("photos/<int:category>", views.CategoryView.as_view(), name="photos_cat"),
#     path("user-list/<int:user>", views.UserView.as_view(), name="user_list"),
#     path("photo-detail/<int:pk>", views.DetailView.as_view(), name="photo_detail"),
#     path("mypage/", views.MypageView.as_view(), name='mypage'),
#     path("photo/<int:pk>/delete/", views.PhotoDeleteView.as_view(), name='photo_delete'),
#     path("photo/<int:pk>/change/", views.ChangePhotoView.as_view(), name='photo_change'),
# ]