from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from GalApp.models import Image
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Image.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)
@api_view(["POST"])
def addItem(request):
    items = Image.objects.all()
    serializer =  ItemSerializer(items, many=True)
    