from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy

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
