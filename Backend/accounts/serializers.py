from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

class RegisterSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','profile_image', 'mobile_phone', 'password1', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'mobile_phone': {'required': True},
            'profile_image': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile_phone=validated_data['mobile_phone'],
            profile_image=validated_data['profile_image'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.mobile_phone = validated_data.get('mobile_phone', instance.mobile_phone)
    #     instance.profile_image = validated_data.get('profile_image', instance.profile_image)
    #     instance.birthdate = validated_data.get('birthdate', instance.birthdate)
    #     instance.facebook_profile = validated_data.get('facebook_profile', instance.facebook_profile)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.save()
    #     return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile_image', 'mobile_phone', 'birthdate','facebook_profile', 'country', 'date_joined', 'is_active', 'deleted_at')
