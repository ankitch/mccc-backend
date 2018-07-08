from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from rest_framework import serializers

from apps.users.models import User, Role, Company


class CustomRegistrationSerializer(serializers.Serializer):
    full_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)

        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address"
                )
            return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'full_name': self.validated_data.get('full_name', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        user.full_name = self.cleaned_data.get('full_name')
        user.save()

        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'settings')


class RoleSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    active = serializers.SerializerMethodField()

    def get_active(self, obj):
        return self.active.id == obj.id if self.active else False

    def __init__(self, *args, **kwargs):
        self.active = kwargs.pop('active', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Role
        fields = ('id', 'type', 'company', 'active')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'email')
