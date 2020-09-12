from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from newuser.forms import userForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth import login, authenticate

# Create your views here.

class MainView(View) :
    def get(self, request):
        return render(request, 'newuser/main.html')


class NewuserCreateView(TemplateView):
    template_name = 'newuser/newuser_form.html'

    def get(self, request):
        userCreationForm = userForm()

        form = {
            'userForm': userCreationForm
        }

        return render(request, self.template_name, form)

    def post(self, request):
        user = userForm(request.POST)

        if user.is_valid():
            user.save()
            user = authenticate(username=user.cleaned_data['username'], password=user.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect('/register')
        else:
            userCreationForm = userForm()
            form = {
                'userForm': userCreationForm
            }
            return render(request, self.template_name, form)
