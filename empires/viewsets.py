from rest_framework import viewsets, filters

from empires.models import Unit
from empires.serializers import UnitSerializer

class UnitViewsets(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Units and enabling user to search for a unit.
    """
    search_fields = ['name', 'age']
    filter_backends = (filters.SearchFilter,)
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    