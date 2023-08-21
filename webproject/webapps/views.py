from django.shortcuts import render
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Modelpost


# Create your views here.

def index(request):
    show = Modelpost.objects.all().order_by('-id')
    context = {'lihat': show}
    return render(request, 'eksWebApps/index.html', context)

class Signup(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'eksWebApps/signup.html'
    success_url = reverse_lazy('login')

class DetailPost(generic.DetailView):
    model = Modelpost
    template_name = 'eksWebApps/detail.html'

class Addpost(generic.CreateView):
    model = Modelpost
    fields = ['judul', 'penulis', 'image', 'konten']
    template_name = 'eksWebApps/add.html'
    
    success_url = reverse_lazy('detail')
    
