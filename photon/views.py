from django.http import request
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def userpost(request):
    posts = Post.objects.filter(user_id = request.user)
    print(posts)
    return render(request,'photon/user_post.html',{'posts':posts})

class PostListView(ListView):
    model = Post
    template_name = "photon/home.html"
    context_object_name = 'posts'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    template_name = "photon/post_detail.html"
    
    


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "photon/post_create.html"
    fields = ['image','title']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = "photon/post_update.html    "
    fields = ['image','title']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "photon/post_delete.html"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


