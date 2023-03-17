from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from user_profile.models import Profile

from users.forms import CustomUserCreationForm, EditProfileForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class EditProfileView(UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('pages:home')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'


class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('pages:home')

    def get_object(self):
        return self.request.user


    # def get_context_data(self, *args, **kwargs):
    #     users = Profile.objects.all()
    #     context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
    #     page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    #     context['page_user'] = page_user
    #     return context


