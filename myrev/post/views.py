from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from post.forms import PostForm
from post.models import Post


# Create your views here.
class CreateView(CreateView):
    template_name='post/create.html'
    form_class=PostForm
    success_url=reverse_lazy('post.list')


class ListPost(ListView):
    template_name='post/list.html'
    model=Post
    context_object_name='posts'


class UpdatePost(UpdateView):
    template_name='post/update.html'
    form_class=PostForm
    success_url=reverse_lazy('post.list')
    queryset = Post.objects.all()


class DeletePost(DeleteView):
    template_name='post/delete.html'
    model=Post
    success_url=reverse_lazy('post.list')
    # queryset = Post.objects.all()


class ShowPost(DetailView):
    model = Post
    template_name='post/show.html'