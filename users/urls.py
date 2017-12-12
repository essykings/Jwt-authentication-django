from django.conf.urls import url, patterns
from .views import authenticate_user, CreateUserAPIView, UserRetrieveUpdateAPIView, UsersCreateView

urlpatterns = [
    url(r'^users/$', UsersCreateView.as_view()),
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^obtain_token/$', authenticate_user),


]
