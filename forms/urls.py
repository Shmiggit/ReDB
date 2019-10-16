from django.urls import path, re_path

from forms.views import index, addProject

urlpatterns = [
    path('addProject', addProject, name='addProject'),
    re_path('', index, name='index'),
]