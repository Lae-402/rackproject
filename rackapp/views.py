from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from .forms import RegisterForm
from .models import Rack
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
class CreatePhotoView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('rack:register_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class RegisterSuccessView(TemplateView):
    template_name = "register_success.html"

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
    # def get_queryset(self):
    #     queryset = Rack.objects.filter(user=self.request.user).order_by('-posted_at') 
    #     return queryset
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TitleView(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        try:
            queryset = Rack.objects.filter(user=self.request.user).order_by('ruby') 
            return queryset
        except:
            return None

class ArtistView(ListView):
    template_name = "index.html"
    def get_queryset(self):
        artist_id = self.kwargs['artist']
        queryset = Rack.objects.filter(user=self.request.user).filter(artist=artist_id).order_by('-posted_at')
        return queryset

class MediaView(ListView):
    template_name = "index.html"
    def get_queryset(self):
        media_id = self.kwargs['media']
        queryset = Rack.objects.filter(user=self.request.user).filter(media=media_id).order_by('-posted_at')
        return queryset