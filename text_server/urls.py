from django.urls import path
from .views import GitHubLinkAPIView, TextAPIView

urlpatterns = [
    path('text/', TextAPIView.as_view(), name='text-api'),
    path('github-link/', GitHubLinkAPIView.as_view(), name='github-link-api'),
]