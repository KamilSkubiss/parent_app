from django.urls import path

from .views import SignUpView, PasswordsChangeView
from users import views as user_view
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    # path('profile/', ShowProfileView.as_view(), name='user_profile')
    path('profile/', user_view.profile, name='profile')
]
