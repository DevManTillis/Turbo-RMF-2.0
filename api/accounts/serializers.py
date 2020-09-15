from rest_framework import serializers
from . import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountProfile
        fields = ('id', 'name', 'username', 'email', 'password',)
        extra_kwargs = {
                        'password' : {'write_only': True},
                        }

    def create(self, validated_data):
        """create and return a new account"""
        account = models.AccountProfile(
            name = validated_data['name'],
            email = validated_data['email'],
            username = validated_data['username'],
        )

        account.set_password(validated_data["password"])
        account.save()
        return account

    # def update(self, instance, validated_data):
    #     for attr, value in validated_data.items():
    #         if attr == 'password':
    #             instance.set_password(value)
    #
    #         else:
    #             setattr(instance, attr, value)
    #
    #     instance.save()
    #     return instance
