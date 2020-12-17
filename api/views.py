from .models import YieldPerKwp
from .serializers import YieldPerKwpSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

class YieldPerKwpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = YieldPerKwp.objects.all()
    serializer_class = YieldPerKwpSerializer
    filter_fields = ['state']

class ExtendedYieldViewSet(viewsets.ViewSet):
    
    def list(self, request):
        state = request.GET.get('state', None)
        capacity = int(request.GET.get('capacity', 1))
        queryset = YieldPerKwp.objects.all()
        if state:            
            queryset = queryset.filter(state=state)        
        serializer = YieldPerKwpSerializer(queryset, many=True)
        for d in serializer.data:
            d['yield'] = capacity * d['yield_kWp']
            del d['yield_kWp']
        return Response(serializer.data)

