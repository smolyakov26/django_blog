from django.urls import path
from .views import HomeView, ArticalDetailView


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', ArticalDetailView.as_view(), name = 'art_details'),
]
