from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic.base import View
from .models import Post
from django.utils import timezone
from .forms import CommentsForm
# Create your views here.

class PostView(generic.ListView):
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(create_as__lte=timezone.now())

class PostDetailView(generic.DetailView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(create_as__lte=timezone.now())

class AddComment(View):
    def post(self,request,pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_ref_id = pk
            form.save()
        return redirect("/")    