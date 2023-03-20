from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from user_profile.models import Profile
from django.contrib import messages

from users.forms import CustomUserCreationForm, EditProfileForm, UserUpdateForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# class EditProfileView(UpdateView):
#     form_class = EditProfileForm
#     success_url = reverse_lazy('pages:home')
#     template_name = 'registration/edit_profile.html'
#
#     def get_object(self):
#         return self.request.user
#
#     def form_valid(self, form):
#         self.object = form.save()
#         return super().form_valid(form)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'


# class ShowProfileView(DetailView):
#     model = Profile
#     template_name = 'registration/user_profile.html'
#     success_url = reverse_lazy('pages:home')

    # def get_object(self):
    #     return self.request.user

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profil został zaktualizowany!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = EditProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/user_profile.html', context)
