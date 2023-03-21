from django.urls import path

from .views import SignUpView, PasswordsChangeView
from users import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password/', PasswordsChangeView.as_view()),
    path('profile/', views.profile, name='profile'),
    path('profile/add_child/', views.add_child, name='add_child')
]
