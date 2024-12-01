from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create-event", views.create_event, name="create_event"),
    path("event-list", views.event_list, name="event_list"),
    path("event-edit/<int:id>", views.event_edit, name="event_edit"),
    path("event-delete/<int:id>", views.event_delete, name="event_delete"),
    path("<slug:slug>", views.details, name="event_details"),# might take str as slug, be aware
]