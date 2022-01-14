from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , DetailView,CreateView
from .models import Post



def home (request) :
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blogg/home.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'blogg/home.html'
    context_object_name = 'posts'
    ordering  = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
   

class PostCreateView(CreateView):
    model = Post
    fields =['title','content']
    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   
def about(request) : 
    return render(request,'blogg/about.html')    