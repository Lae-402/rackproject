from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from .forms import RegisterForm, ArtistForm
from .models import Rack, Artist
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        try:
            queryset = Rack.objects.filter(user=self.request.user).order_by('ruby') 
            return queryset
        except:
            return None

@method_decorator(login_required, name="dispatch")
class RegisterArtistView(CreateView):
    form_class = ArtistForm
    template_name = "artist_register.html"
    success_url = reverse_lazy('rackapp:artist_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)    
    # def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    #     return super().post(request, *args, **kwargs)

class ArtistSuccessView(TemplateView):
    template_name = "artist_success.html"

@method_decorator(login_required, name="dispatch")
class AddRackView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('rackapp:register_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class RegisterSuccessView(TemplateView):
    template_name = "register_success.html"

class HowToView(TemplateView):
    template_name = "howto.html"

class RackView(ListView):
    template_name = 'rack.html'
    def get_queryset(self):
        try:
            queryset = Rack.objects.filter(user=self.request.user).order_by('-posted_at') 
            return queryset
        except:
            return None

class DetailView(DetailView):
    template_name = "detail.html"
    model = Rack

class RackDeleteView(DeleteView):
    model = Rack
    template_name = "rack_delete.html"
    success_url = reverse_lazy('rackapp:rack')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TitleView(ListView):
    template_name = 'rack.html'
    def get_queryset(self):
        try:
            queryset = Rack.objects.filter(user=self.request.user).order_by('ruby') 
            return queryset
        except:
            return None

class ArtistView(ListView):
    template_name = "rack.html"
    def get_queryset(self):
        artist_id = self.kwargs['artist']
        queryset = Rack.objects.filter(user=self.request.user).filter(artist=artist_id).order_by('-posted_at')
        return queryset

class MediaView(ListView):
    template_name = "rack.html"
    def get_queryset(self):
        media_id = self.kwargs['media']
        queryset = Rack.objects.filter(user=self.request.user).filter(media=media_id).order_by('-posted_at')
        return queryset