from rest_framework import serializers
from .models import TransferEvent


class TransferEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferEvent
        fields = "__all__"
