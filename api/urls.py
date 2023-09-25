from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view(), name="upload"),
    path('files/', views.FileListView.as_view(), name="files"),
]
