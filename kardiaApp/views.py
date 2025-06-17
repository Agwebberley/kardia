from rest_framework import viewsets
from .models import ZettelCard, CustomField, CustomFieldValue
from .serializers import ZettelCardSerializer, CustomFieldSerializer, CustomFieldValueSerializer

class ZettelCardViewSet(viewsets.ModelViewSet):
    queryset = ZettelCard.objects.all()
    serializer_class = ZettelCardSerializer

class CustomFieldViewSet(viewsets.ModelViewSet):
    queryset = CustomField.objects.all()
    serializer_class = CustomFieldSerializer

class CustomFieldValueViewSet(viewsets.ModelViewSet):
    queryset = CustomFieldValue.objects.all()
    serializer_class = CustomFieldValueSerializer