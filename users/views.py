from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from user_profile.models import Child, Task
from users.forms import CustomUserCreationForm, EditProfileForm, UserUpdateForm, ChildAddForm, TaskAddForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'


@login_required
def profile(request):
    children = []
    tasks = []
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
        children = Child.objects.filter(user=request.user).all()
        tasks = Task.objects.filter(child__in=children.all())

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'children': children,
        'tasks': tasks
    }

    return render(request, 'users/user_profile.html', context)


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
    return render(request, 'users/child_add.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskAddForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            task.child.add(form.cleaned_data.get('child'))
            messages.success(request, f'{task.title} został dodany do Twojego profilu!')
            return redirect('profile')
    else:
        form = TaskAddForm(request.user)

    context = {
        'form': form
    }
    return render(request, 'users/task_new.html', context)


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, f'{task.title} został usunięty!')
    return redirect('profile')
