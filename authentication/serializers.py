from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    repeat = serializers.CharField(
        max_length=65, min_length=3, style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeat']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})

        return super().validate(attrs)

    def save(self):
        user = User(
            username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        repeat = self.validated_data['repeat']

        if password != repeat:
            raise serializers.ValidationError(
                {'password': 'Password did not match'})
        user.set_password(password)
        user.is_active = False
        user.save()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=3, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']
