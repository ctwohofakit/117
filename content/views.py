from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Tag, Status, Project
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)



# Create your views here.
# Create project list view, filter by publish,sort by date
class Projects_list_view(ListView):
    template_name='content/project_list.html'
    model=Project
    context_object_name="projects"
# the context_object_name = "projects", just assign the varible name to the list(object_list)
#only need to declare once

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        published=Status.objects.get(name="published")
        context["project_list"]=(
            Project.objects
            .filter(status=published)
            .order_by("date").reverse()
        )
        return context
    
# Create draft view, filter by draft, only author can see
class Draft_Project_View(ListView):
    template_name='content/project_list.html'
    model=Project
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        draft=Status.objects.get(name="draft")
        context["project_list"]=(
            Project.objects
            .filter(status=draft)
            .filter(author=self.request.user)
        #only author self publish post can view the autor post, other author can't see
            .order_by("date").reverse()
        )
        return context
    
# Create Archived view, filter by Archived, only author can see

class Archived_Project_View(LoginRequiredMixin,ListView):
    template_name='content/project_list.html'
    model=Project

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        archived=Status.objects.get(name="archived")
        context["project_list"]=(
            Project.objects
            .filter(status=archived)
            .order_by("date").reverse()
        )
        return context

# Create Create view, only author can create
#superClass is stay on the right--CreateView
class Create_Project_View(LoginRequiredMixin,CreateView):
    template_name='content/new.html'
    model=Project
    fields=["static","animated","title","website","description","date","tags","status"]
    success_url=reverse_lazy('list')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    


# Create Detail view, only author can create
class Detail_Project_view(DetailView):
    template_name='content/detail.html'
    model=Project


# Create Edit view, only author can Edit
class Update_Project_View(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    template_name='content/edit.html'
    model=Project
    fields=["static","animated","title","website","description","date","tags","status"]

    def test_func(self):
        project=self.get_object()
        return project.author==self.request.user
    success_url = reverse_lazy("list")
    
# Create delete view, only author can deletle
class Delete_Project_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name='content/delete.html'
    model=Project
    success_url=reverse_lazy('list')

    def test_func(self):
        project=self.get_object()
        return project.author==self.request.user
