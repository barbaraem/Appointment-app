from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView

from reminders.models import Appointment


class AppointmentListView(ListView):
    """generic view - shows a list of appointments"""
    model = Appointment


class AppointmentDetailView(DetailView):
    """generic view - shows a single appointment"""
    model = Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """generic view for creating a form and save a new appointment"""
    model = Appointment
    fields = ["name", "phone_number", "time", "time_zone"]
    success_message = "Appointment successfully created"


class AppointmentUpdateView(UpdateView):
    """generic view for edit existing appointments"""
    model = Appointment
    fields = ["name", "phone_number", "time", "time_zone"]
    success_message = "Appointment successfully updated"


class AppointmentDeleteView(DeleteView):
    """Asks users to confirm deletion of an appointment"""
    model = Appointment
    success_url = reverse_lazy('list_appointments')







