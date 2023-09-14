

# Create your views here.
from rest_framework import viewsets

from .serializer import OfferSerializer
from .models import Offer


# Create your views here.

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('name')
    serializer_class = OfferSerializer
