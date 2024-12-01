from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create-event", views.create_event, name="create_event"),
    path("event-list", views.event_list, name="event_list"),
    path("participant-list", views.participant_list, name="participant_list"),
    path("delete-participation/<int:id>", views.delete_participation, name="delete_participation"),
    path("event-edit/<int:id>", views.event_edit, name="event_edit"),
    path("event-delete/<int:id>", views.event_delete, name="event_delete"),
    path("participate/<int:id>", views.participate, name="participate"),
    path("<slug:slug>", views.details, name="event_details"),
]