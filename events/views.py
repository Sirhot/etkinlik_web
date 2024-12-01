from django.shortcuts import get_object_or_404, redirect, render
from events.forms import EventCreateForm, EventEditForm
from .models import Event, Participant
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def index(request):
    events = Event.objects.filter(isActive=1)
    
    paginator = Paginator(events,2)
    page = request.GET.get("page",1)
    page_obj = paginator.get_page(page)
    
    return render(request,"events/index.html", {
        "page_obj": page_obj
    })

def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q = request.GET["q"]
        events = Event.objects.filter(isActive=1, name__contains=q).order_by("date")
    else:
        return redirect("/events")
    
    paginator = Paginator(events,2)
    page = request.GET.get("page",1)
    page_obj = paginator.get_page(page)
    
    return render(request, "events/search.html", {
        "page_obj": page_obj
    })

@login_required()
def create_event(request):
    if request.method == "POST":
        # Usage of forms.py in Django
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/events")
    # If there is a posted req without inputs, it won't create new form 
    else:
        form = EventCreateForm() 
    return render(request, "events/create-event.html", {"form":form})

@login_required()
def event_list(request):
    events = Event.objects.filter(isActive=1)
    return render(request,"events/event-list.html", {
        "events": events
    })

def event_edit(request,id):
    event = get_object_or_404(Event, pk=id)
    
    if request.method == "POST":
        form = EventEditForm(request.POST, instance=event)
        form.save()
        return redirect("event_list")
    else:
        form = EventEditForm(instance=event)
    
    return render(request,"events/edit-event.html",{"form":form})

def event_delete(request,id):
    event = get_object_or_404(Event, pk=id)
    
    if request.method == "POST":
        event.delete()
        return redirect("event_list")
    
    return render(request, "events/event-delete.html",{"event":event})

def details(request, slug):
    event = get_object_or_404(Event, slug=slug)
    participants = Participant.objects.filter(event=event)
    
    context = {
        "event": event,
        "participants": participants,
    }
    
    return render(request, "events/details.html", context)

@login_required()
def participate(request, id):
    event = get_object_or_404(Event, id=id)

    if Participant.objects.filter(user=request.user, event=event).exists():
        messages.add_message(request, messages.WARNING, "Bu etkinliğe önceden katıldınız.")
        return redirect("event_details", slug=event.slug)

    Participant.objects.create(user=request.user, event=event)
    messages.add_message(request, messages.SUCCESS, "Etkinliğe katıldınız!")
    return redirect("event_details", slug=event.slug)

@login_required()
def participant_list(request):
    participations = Participant.objects.filter(user=request.user).select_related("event")
    
    return render(request, "events/participant-list.html", {"participations": participations})

@login_required
def delete_participation(request, id):
    participation = get_object_or_404(Participant, id=id, user=request.user)
    
    if request.method == "POST":
        participation.delete()
        messages.success(request, "Etkinlikten ayrıldınız.")
        return redirect("participant_list")
    
    return render(request, "events/delete-participation.html", {"participation": participation})
