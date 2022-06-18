from rest_framework import serializers
from GalApp.models import Image

class ItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Image
        fields = ('id','caption','image')

