from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from user_profile.models import Child
from users.forms import CustomUserCreationForm, EditProfileForm, UserUpdateForm, ChildAddForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'


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
        children = Child.objects.filter(user=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'children': children,
    }

    return render(request, 'registration/user_profile.html', context)


@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildAddForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.user = request.user
            child.save()
            messages.success(request, f'{child.name} został dodany do Twojego profilu!')
            return redirect('profile')
    else:
        form = ChildAddForm()

    context = {
        'form': form
    }
    return render(request, 'registration/child_add.html', context)
