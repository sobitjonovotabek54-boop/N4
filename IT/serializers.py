
from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=CustomUser
        fields=['username','password','first_name','last_name','phone_number','bio','telegram_username',]
        read_only_fields=['id']
        


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            bio=validated_data["bio"],
            telegram_username=validated_data.get("telegram_username"),
            password=validated_data["password"],
        )
        return user   