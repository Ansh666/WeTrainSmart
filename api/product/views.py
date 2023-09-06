from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import ProductSerializer
from .models import Product


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
   
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]
