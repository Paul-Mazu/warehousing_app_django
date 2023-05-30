from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import SignUpView, CustomLogin, CustomLogout


app_name = "account"

urlpatterns = [
    path("login/", CustomLogin.as_view(), name="login"),
    path("logout/", CustomLogout.as_view(), name="logout"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
