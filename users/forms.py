from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import DateInput

from user_profile.models import Profile, Child


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
