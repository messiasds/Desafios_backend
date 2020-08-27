from rest_framework import serializers

class NewURLSerializer(serializers.Serializer):

    newUrl = serializers.CharField(source='new_url')
    expirationDate = serializers.DateField(source='validade')


class OriginalURlSerializer(serializers.Serializer):

    originalUrl = serializers.CharField(source='original_url')
