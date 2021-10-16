from rest_framework import serializers
from . models import *


class ServicesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('__all__')