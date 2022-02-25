import django_filters
from .models import *

class Datafilter(django_filters.Filterset):
    class Meta:
        model = status
        fields = '__all__'