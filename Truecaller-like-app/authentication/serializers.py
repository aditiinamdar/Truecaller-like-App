
# spam_app/serializers.py
from urllib import request
from rest_framework import serializers


from .models import Contact, CustomUser, Spam
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','name','phone_number','email','spam_likelihood','password']  
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.is_active = True
        if password is not None:
            user.set_password(password)

        user.save()
        return user

class ContactSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_phone_number','spam_likelihood','user']  

class AddContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_phone_number','spam_likelihood','user']  


class NamesearchcontactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_phone_number','spam_likelihood','user']  

class NamesearchuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name','phone_number','email','spam_likelihood']  

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = '__all__'

