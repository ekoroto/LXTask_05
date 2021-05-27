from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']

    def create(self, validated_data):
        """
            Keeping password in hash form,
            that allows us to use corresponding user for authorization.
        """
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
