from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from register.models import Profile, Account
from django.urls import reverse_lazy
from register.forms import ProfileForm, AccountForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DeleteView, DetailView, CreateView, UpdateView
from random import randint
import joblib

# Create your views here.

class LoginHomeView(View) :
    model = Profile
    template_name = 'register/home.html'

    def get(self, request):
        profiles = Profile.objects.all()
        accounts = Account.objects.all()
        context= {
            'profiles': profiles, 'accounts': accounts
        }
        return render(request, self.template_name, context)


class ProfileView(DetailView):
    model = Profile
    template_name = "register/profile_detail.html"

class ProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'register/profile_form.html'

    def get(self, request):
        profileCreationForm = ProfileForm()

        form = {
            'profileForm': profileCreationForm
        }

        return render(request, self.template_name, form)

    def post(self, request):
        profile = ProfileForm(request.POST, request.FILES)

        if profile.is_valid():
            profile_created = profile.save(commit=False)
            profile_created.user = self.request.user
            profile_created.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Error occurred")

class ProfileDeleteView(DeleteView):
    model = Profile
    #template_name = 'register/profile_delete.html'
    success_url = reverse_lazy('/')

class ProfileUpdateView(UpdateView):
    model = Profile
    #template_name = 'register/profile_delete.html'
    success_url = reverse_lazy('/')

class AccountCreateView(LoginRequiredMixin, CreateView):
    template_name = 'register/account_form.html'

    def get(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)
        profileCreationForm = ProfileForm(instance=profile)
        accountCreationForm = AccountForm()
        form = {
            'profileForm': profileCreationForm, 'accountForm': accountCreationForm
        }
        return render(request, self.template_name, form)

    def post(self, request):
        account = AccountForm(request.POST)

        if account.is_valid():
            account_created = account.save(commit=False)
            account_created.owner = self.request.user
            account_created.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Error occurred")

class AccountDeleteView(DeleteView):
    model = Account
    #template_name = 'register/profile_delete.html'
    success_url = reverse_lazy('/')

class AccountDetailView(DetailView):
    model = Account
    template_name = "register/profile_detail.html"

class ClassifierOCR(View):
    model = Profile
    template_name = 'register/classifier.html'
    def get(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)

        cnn = joblib.load('finalised_model_CNN.pkl')
        ans = cnn.predict(profile.docImage)

        ctx = {
            'answer': ans
            }

        return render(request, self.template_name, ctx)

"""def AccountDelete(self, request, pk):
    model = Account
    success_url = reverse_lazy('/')

    obj = get_object_or_404(Account, id = pk, owner = self.request.user)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    else:
        return HttpResponse("Error occurred")"""