# save/urls.py

from django.urls import path
from .views import save_spam

urlpatterns = [
    path('spam/save/', save_spam, name='save_spam'),
]
