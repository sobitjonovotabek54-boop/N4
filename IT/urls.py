from django.urls import path
from .views import RegisterAPIView

urlpatterns = [
    path('telegram/', RegisterAPIView.as_view()),
]