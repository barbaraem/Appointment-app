from django.conf.urls import include, url
from django.contrib import admin

from reminders.views import AppointmentCreateView, AppointmentListView, AppointmentDeleteView, AppointmentDetailView, \
    AppointmentUpdateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'appointment_reminders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # List and detail of appointments
    url(r'^$', AppointmentListView.as_view(), name='list_appointments'),
    url(r'^/(?P<pk>[0-9]+)$', AppointmentDetailView.as_view(), name='view_appointment'),

    # CRUD of appointments
    url(r'^appointment_form$', AppointmentCreateView.as_view(), name='new_appointment'),
    url(r'^/(?P<pk>[0-9]+)/edit$', AppointmentUpdateView.as_view(), name='edit_appointment'),
    url(r'^/(?P<pk>[0-9]+)/delete$', AppointmentDeleteView.as_view(), name='delete_appointment'),
]
