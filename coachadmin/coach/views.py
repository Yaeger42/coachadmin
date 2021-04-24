from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth import views as auth_views


from coach.models import Coach
from coach.forms import CreateCoachForm

# Create your views here.
class CreateCoachView(LoginRequiredMixin, CreateView):
    template_name = 'coach/new.html'
    form_class = CreateCoachForm
    success_url = reverse_lazy('coach:feed')

        
class CoachFeedView(LoginRequiredMixin, ListView):
    template_name = 'coach/feed.html'
    model = Coach 
    ordering = ('-created')
    context_object_name = 'coaches'

class CoachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    success_url = reverse_lazy('coach:feed')



class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'index.html'
    success_url = reverse_lazy('/')


class EditCoachView(LoginRequiredMixin, UpdateView):
    model = Coach
    fields = ['firstName', 'lastName', 'email', 'phone', 'location', 'hobby']
    context_object_name = 'coach'
    template_name = 'coach/edit.html'
    success_url = reverse_lazy('coach:feed')

