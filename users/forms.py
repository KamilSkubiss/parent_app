from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import DateInput

from user_profile.models import Profile, Child, Task


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)


class EditProfileForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Profile
        fields = ('age', 'bio', 'avatar')


class ChildAddForm(forms.ModelForm):
    date_of_birth = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = Child
        fields = ('name', 'date_of_birth',)


class TaskAddForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=1000)
    due_date = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    child = forms.ModelChoiceField(queryset=Child.objects.none())

    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'child')

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child'].queryset = Child.objects.filter(user=user)

