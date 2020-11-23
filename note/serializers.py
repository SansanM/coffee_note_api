from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class UserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')

class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Note
        fields ="__all__"
        read_only_fields = ('created_at', 'updated_at')

class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Note
        fields ="__all__"
        read_only_fields = ("title","uuid","body","sanmi","nigami","like","user","public",'created_at', 'updated_at')