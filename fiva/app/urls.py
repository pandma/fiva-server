from django.urls import path
from .views.Register_views import RegisterView, LoginView, VerifyUserView, LogoutView
from .views.Comapnies_views import companies_views
from .views.Maximeter_up_to_50_views import Maximeter_up_to_50Views
from .views.Maximeter_50_plus_views import Maximeter_50_plusViews


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', VerifyUserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('companies', companies_views.as_view()),
    path('les50', Maximeter_up_to_50Views.as_view()),
    path('max50', Maximeter_50_plusViews.as_view()),
]
