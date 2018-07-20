from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from twilio.rest import Client

import arrow

from reminders.models import Appointment


account_sid = "AC1b37b130c7442312a7214aee4c96066b"
auth_token = "9e1aa53e509b62e5101abf31fc062235"

client = Client(account_sid, auth_token)


@shared_task
def send_sms_reminder(appointment_id):
    """Send a SMS reminder using Twilio """
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = 'Hi {0}. You have an appointment coming up at {1}.'.format(
        appointment.name,
        appointment_time.format('h:mm a')
    )

    message = client.messages.create(
        body=body,
        to=appointment.phone_number,
        from_=settings.TWILIO_NUMBER,
    )
