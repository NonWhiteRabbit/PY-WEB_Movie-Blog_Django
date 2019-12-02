from django.urls import path
from home.views import HomeView, SingleView, LoginView, MovieView, RegisterView

urlpatterns = [
    path('single', SingleView.as_view(), name='single'),
    path('', HomeView.as_view(), name='home'),	
    path('login', LoginView.as_view(), name='login'),
    path('movie', MovieView.as_view(), name='movie'),
    path('register', RegisterView.as_view(), name='register')
]