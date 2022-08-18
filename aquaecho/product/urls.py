from django.urls import path
from .views import Index

urlpatterns = [
    path(route='', view=Index.as_view()),
]
