from rest_framework import serializers
from .models import TesterModel

class TesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TesterModel
        #fields = '__all__'
        fields = ('id', 'name', 'element')
        