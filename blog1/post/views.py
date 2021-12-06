from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from comments.models import Comment
from post.forms import CommentForm
from post.models import Blog


class PostListView(ListView):
    model = Blog
    template_name = 'blog.html'


def post_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    model = Comment()
    if request.POST:
        model.blog = blog
        model.comment = request.POST.get('comment')
        model.author = request.user
        model.save()
    comments = Comment.objects.filter(blog=blog)
    print(comments)
    return render(request, 'detail-blog.html', {'blog': blog, 'comments': comments})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'body', 'image']
    template_name = 'add-blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'body', 'image']
    template_name = 'update-blog.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'delete-blog.html'
    success_url = reverse_lazy('blog-page')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
