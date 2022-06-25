from django.urls import path
from .views.Register_views import RegisterView,LoginView,VerifyUserView, LogoutView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', VerifyUserView.as_view()),
    path('logout', LogoutView.as_view()),
]
