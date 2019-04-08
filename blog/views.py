from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.views.generic import CreateView

from blog.forms import BlogForm

class NewBlogView(CreateView):
    form_class = BlogForm
    template_name = 'blog_settings.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)
        blog_obj.save()

        return HttpResponseRedirect(reverse('home'))