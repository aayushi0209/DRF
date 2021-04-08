from . import views
from django.urls import path

urlpatterns = [
      path('Register/', views.Registerapi),
      path('Login/', views.Login.as_view(), name="api_auth"),
      path('Dashboard/', views.userGetViewSet.as_view(), name="user_get"),
]


