from django.shortcuts import render
from rest_framework import viewsets
from .serializers import YieldPerKwpSerializer
from .models import YieldPerKwp

class YieldPerKwpViewSet(viewsets.ModelViewSet):
    queryset = YieldPerKwp.objects.all()
    serializer_class = YieldPerKwpSerializer
    filter_fields = ['state']

