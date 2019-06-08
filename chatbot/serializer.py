from rest_framework import serializers


class MyViewSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=256)

    def create(self, validated_data):
      return Task(**)