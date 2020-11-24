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
    user = UserSerializer(read_only=True)
    def validate_title(self,validated_data):
        if(len(validated_data) == 0):
            raise serializers.ValidationError("タイトルは必須です")
        if(50 < len(validated_data)):
            raise serializers.ValidationError("タイトルは50文字以内にしてください")
        return validated_data

    def validate_sanmi(self,validated_data):
        if(validated_data < 0 or 5 < validated_data):
            raise serializers.ValidationError("1から5の範囲で入力してください")
        return validated_data

    def validate_nigami(self,validated_data):
        if(validated_data < 0 or 5 < validated_data):
            raise serializers.ValidationError("1から5の範囲で入力してください")
        return validated_data

    def validate_like(self,validated_data):
        if(validated_data < 0 or 5 < validated_data):
            raise serializers.ValidationError("1から5の範囲で入力してください")
        return validated_data

    def validate_public(self,validated_data):
        print(validated_data)
        if(not(validated_data == "true" or validated_data == "false")):
            raise serializers.ValidationError("trueかfalseの入力にしてください")
        return validated_data
    
    class Meta:
        model = Note
        user = UserSerializer(read_only=True)
        fields ="__all__"
        read_only_fields = ('created_at', 'updated_at',"user__username")

class NotePublicSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Note
        fields ="__all__"
        read_only_fields = ("title","uuid","body","sanmi","nigami","like","user","public",'created_at', 'updated_at')


        
