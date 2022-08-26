from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("save", views.save, name="save"),
    path("randomPage",views.randomPage, name='randomPage'),
    path("editPage",views.editPage, name='editPage'),
    path("deletePage",views.deletePage, name='deletePage'),
    path("saveEdit",views.saveEdit, name='saveEdit')
]