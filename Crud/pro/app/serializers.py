from rest_framework import serializers
from app.models import MobileModel


class MobileDrf(serializers.ModelSerializer):
    class Meta:
        model=MobileModel
        fields='__all__'