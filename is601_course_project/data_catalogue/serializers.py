from .models import DataSetDesc
from rest_framework import serializers


class DataSetDescSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSetDesc
        fields = ['name', 'desc', 'environment_type', 'dataid']


