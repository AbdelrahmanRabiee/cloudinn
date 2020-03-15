from rest_framework import serializers
from rest_framework.fields import SkipField

from collections import OrderedDict
from operator import itemgetter

from empires.models import Cost, Unit


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'

    def to_representation(self, instance):
        """
        Remove null values from API response
        """
        ret = super().to_representation(instance)
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret     


class UnitSerializer(serializers.ModelSerializer):
    cost = CostSerializer(read_only=True)
    class Meta:
        model = Unit
        fields = '__all__' 

    def to_representation(self, instance):
        """
        Remove null values from API response
        """
        ret = super().to_representation(instance)
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret          