from django.core.urlresolvers import reverse
from django.db import models
from timezone_field.fields import TimeZoneField


class Appointment(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=9)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default="Europe/Warsaw")

    # additional fields:
    task_id = models.CharField(max_length=150, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return "Appointment number:{} - {} ".format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('view_appointment', args=[str(self.id)])





